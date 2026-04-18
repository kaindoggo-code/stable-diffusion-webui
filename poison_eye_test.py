import urllib.request
import json
import base64
import os
import time

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
payload = {
    "prompt": "masterpiece, amazing quality, <lora:vilefox_v1:0.8>, vilefox, solo, male, anthro, orange fur, white muzzle, teal eyes, black sclera, teal poison marks in eyes, dripping, red cloak, muscular, extreme detail, 04_ART style",
    "negative_prompt": "low quality, bad anatomy, human, text, blue fur",
    "steps": 28,
    "cfg_scale": 5.0,
    "width": 896,
    "height": 1152,
    "sampler_name": "Euler a"
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        img_data = base64.b64decode(res['images'][0])
        out_path = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/vilefox_poison_eye_test.png")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(img_data)
        print(f"SUCCESS: {out_path}")
except Exception as e:
    print(f"FAILED: {e}")
