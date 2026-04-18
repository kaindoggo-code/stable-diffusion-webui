import urllib.request
import json
import base64
import os

url_options = "http://127.0.0.1:7860/sdapi/v1/options"
url_txt2img = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# 1. SWITCH MODEL TO NOVA
opt_payload = {"sd_model_checkpoint": "novaFurryXL_ilV170.safetensors"}
req = urllib.request.Request(url_options, data=json.dumps(opt_payload).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='POST')
try:
    urllib.request.urlopen(req)
    print("Switched to Nova Furry XL.")
except Exception as e:
    print(f"Option Switch Failed: {e}")

# 2. RENDER BALANCED LINEART
payload = {
    "prompt": "masterpiece, amazing quality, <lora:vilefox_v1:0.85>, vilefox, solo, male, anthro, orange fur, white muzzle, teal eyes, black sclera, black tendril tongue, blue saliva, small curved horns with teal and black stripes and golden runes, torn damaged red cloak, muscular build, extreme detail, 04_ART style",
    "negative_prompt": "armor, mechanical, robot, low quality, bad anatomy, text, blue fur, human, female",
    "steps": 28,
    "cfg_scale": 5.0,
    "width": 896,
    "height": 1152,
    "sampler_name": "Euler a"
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url_txt2img, data=data, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        img_data = base64.b64decode(res['images'][0])
        out_path = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/vilefox_NOVA_RECOVERY.png")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(img_data)
        print(f"SUCCESS: {out_path}")
except Exception as e:
    print(f"FAILED: {e}")
