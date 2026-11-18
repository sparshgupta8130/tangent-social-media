"""Step 1: extend each 4:5 still (1856x2304) to a square 3300x3300 'stage' canvas.

The original sits pixel-exact in the centre (x 722..2578, y 498..2802); Nano Banana Pro
(gemini-3-pro-image, Gemini API) only paints the border: more wall above, floor below and
gallery to each side. The side margins let the camera glide laterally between exhibits; the
top/bottom margins make a full-width 9:16 frame possible.

    python outpaint.py            # all of 02..09, skipping ones already in work/gen/
    python outpaint.py 05 09      # just these
Needs GEMINI_API_KEY in the environment (never printed, never written to disk).
The raw API returns are kept in work/gen/ (gitignored); the composited canvases go to
work/canvas/slide-NN.png via compose_canvas() in stage.py.
"""
import base64, json, os, sys, time, urllib.request
import cv2, numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '2026-11-museum-of-men', 'assets', 'gen', 'pick')
GEN = os.path.join(HERE, 'work', 'gen'); os.makedirs(GEN, exist_ok=True)
CW = CH = 3300
OX, OY = (CW - 1856) // 2, (CH - 2304) // 2  # 722, 498
MODEL = 'gemini-3-pro-image'
URL = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'

PROMPT = (
    "This is a photograph of a minimalist contemporary art museum, placed in the centre of a larger "
    "square canvas. The flat mid-grey border around it is empty canvas. Outpaint: replace ONLY the flat grey "
    "border with a seamless, photorealistic continuation of the same room - more of the same clean warm-white "
    "wall above, more of the same pale grey polished concrete floor below, and more of the same empty gallery "
    "to the left and right (plain walls, room corners). Match the lighting, colour, grain, perspective and lens "
    "exactly. Continue any plinth or object that touches the edge of the photo naturally. Do not add any new "
    "objects, plinths, people, text, signs, frames, lights or logos. Keep the original photo in the centre "
    "completely unchanged, at the same position and size. Output the full square image.")


def padded(n):
    im = cv2.imread(os.path.join(SRC, f'slide-{n}.png'))
    can = np.full((CH, CW, 3), 128, np.uint8)
    can[OY:OY + 2304, OX:OX + 1856] = im
    return can


def call(n):
    can = padded(n)
    small = cv2.resize(can, (2048, 2048), interpolation=cv2.INTER_AREA)
    ok, jpg = cv2.imencode('.jpg', small, [cv2.IMWRITE_JPEG_QUALITY, 92])
    body = {
        'contents': [{'parts': [
            {'inline_data': {'mime_type': 'image/jpeg', 'data': base64.b64encode(jpg.tobytes()).decode()}},
            {'text': PROMPT}]}],
        'generationConfig': {'responseModalities': ['IMAGE'],
                             'imageConfig': {'aspectRatio': '1:1', 'imageSize': '4K'}},
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method='POST', headers={
        'Content-Type': 'application/json', 'x-goog-api-key': os.environ['GEMINI_API_KEY']})
    with urllib.request.urlopen(req, timeout=600) as r:
        res = json.load(r)
    for c in res.get('candidates', []):
        for p in c.get('content', {}).get('parts', []):
            d = p.get('inline_data') or p.get('inlineData')
            if d:
                return base64.b64decode(d['data']), d.get('mime_type') or d.get('mimeType')
    raise RuntimeError('no image in response: ' + json.dumps(res)[:400])


if __name__ == '__main__':
    todo = sys.argv[1:] or [f'{i:02d}' for i in range(2, 10)]
    for n in todo:
        k = 1
        while os.path.exists(os.path.join(GEN, f'slide-{n}-o{k}.jpg')):
            k += 1
        if k > 1 and len(sys.argv) == 1:
            print(n, 'exists, skip'); continue
        for attempt in range(3):
            try:
                data, mime = call(n); break
            except Exception as e:  # noqa: BLE001
                print(n, 'retry', attempt, str(e)[:200]); time.sleep(10)
        else:
            continue
        arr = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
        out = os.path.join(GEN, f'slide-{n}-o{k}.jpg')
        cv2.imwrite(out, arr, [cv2.IMWRITE_JPEG_QUALITY, 95])
        print(n, mime, arr.shape, '->', out)
