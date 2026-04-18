import urllib.request
import json
import base64
import os
import time

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
output_dir = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/AUDIT")
os.makedirs(output_dir, exist_ok=True)

prompts = [
    {
        "name": "HERO_ART",
        "prompt": "masterpiece, amazing quality, <lora:vilefox_v1:0.8>, vilefox, solo, male, anthro, teal eyes, black sclera, orange fur, white muzzle, red cloak, muscular build, dynamic pose, cinematic lighting, 04_ART style, dramatic shadows",
    },
    {
        "name": "NSFW_ANATOMY",
        "prompt": "masterpiece, amazing quality, <lora:vilefox_v1:1.0>, vilefox, solo, male, anthro, teal eyes, black sclera, standing nude, muscular build, black canine penis, large sheath, knotting, textured, extreme detail, cinematic lighting, 04_ART style",
    }
]

for p in prompts:
    print(f"Running {p['name']} check...")
    payload = {
        "prompt": p['prompt'],
        "negative_prompt": "low quality, bad anatomy, human, text",
        "steps": 28,
        "cfg_scale": 5.0,
        "width": 1024,
        "height": 1024,
        "sampler_name": "Euler a"
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            img_data = base64.b64decode(res['images'][0])
            out_path = os.path.join(output_dir, f"vilefox_{p['name']}.png")
            with open(out_path, "wb") as f:
                f.write(img_data)
            print(f"  SUCCESS: {out_path}")
    except Exception as e:
        print(f"  FAILED: {e}")

print("AUDIT COMPLETE.")
