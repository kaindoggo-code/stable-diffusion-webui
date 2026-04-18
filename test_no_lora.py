import urllib.request
import json
import base64
import os
import time

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
payload = {
    "prompt": "masterpiece, amazing quality, score_9, score_8_up, source_furry, vilefox, solo, anthro, male, orange fur, white muzzle, brown hair, blue eyes, black sclera, red cloak, muscular, extreme detail, 04_ART style",
    "negative_prompt": "low quality, bad anatomy, human, text",
    "steps": 28,
    "cfg_scale": 4.5,
    "width": 1024,
    "height": 1024,
    "sampler_name": "Euler a"
}

data = json.dumps(payload).encode('utf-8')
headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(url, data=data, headers=headers)

start = time.time()
try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        img_data = base64.b64decode(res['images'][0])
        out_path = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/no_lora_test.png")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(img_data)
        elapsed = time.time() - start
        print(f"SUCCESS: Image rendered WITHOUT LORA in {elapsed:.2f} seconds. Saved to {out_path}")
except Exception as e:
    print(f"FAILED: {e}")
