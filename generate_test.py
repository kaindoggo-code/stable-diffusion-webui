import urllib.request
import json
import base64
import os
import time

url = "http://127.0.0.1:7861/sdapi/v1/txt2img"
payload = {
  "prompt": "masterpiece, amazing quality, score_9, score_8_up, source_furry, <lora:vilefox_v1:1.0>, vilefox, solo, male, anthro, full body, orange fur, white muzzle, brown hair, blue eyes, black sclera, grinning, sharp teeth, red cloak, standing nude, muscular build, extreme detail, cinematic lighting, dramatic shadows, 04_ART style",
  "negative_prompt": "low quality, bad anatomy, human, text",
  "steps": 28,
  "cfg_scale": 4.5,
  "width": 1024,
  "height": 1024,
  "sampler_name": "Euler a"
}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})

start = time.time()
print("Sending request to Forge API...")
try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        img_data = base64.b64decode(res['images'][0])
        out_path = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/vilefox_v5_test.png")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(img_data)
        print(f"Success! Image saved to {out_path} in {time.time()-start:.2f} seconds.")
except Exception as e:
    print(f"Error: {e}")
