import urllib.request
import json
import base64
import os

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
payload = {
    "prompt": "masterpiece, amazing quality, <lora:vilefox_v1:0.7>, vilefox, solo, female, (breasts:1.3), (large breasts:1.2), curvy body, long eyelashes, orange fur, white muzzle, 2 yellow v shape markings on muzzle, teal eyes, black sclera, black tendril tongue, blue saliva, striped horns, golden runes, torn red cloak, extreme detail, 04_ART style",
    "negative_prompt": "male, anthro male, (penis:1.5), (beard:1.2), masculine, flat chest, boy, low quality, bad anatomy, text",
    "steps": 30,
    "cfg_scale": 6.0,
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
        out_path = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/vilefox_FEM_TEST_SUCCESS.png")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(img_data)
        print(f"SUCCESS: {out_path}")
except Exception as e:
    print(f"FAILED: {e}")
