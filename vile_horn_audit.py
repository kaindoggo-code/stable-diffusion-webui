import urllib.request
import json
import base64
import os

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
rune_weights = [0.8, 1.2, 1.5]

output_base = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/HORN_AUDIT")
os.makedirs(output_base, exist_ok=True)

print("HORN CONSISTENCY AUDIT STARTING...")

for rw in rune_weights:
    name = f"rune_weight_{rw}"
    print(f"Testing {name}...")
    payload = {
        "prompt": f"masterpiece, amazing quality, <lora:vilefox_v1:0.9>, vilefox, solo, portrait, (golden runes on horns:{rw}), (teal and black striped horns:1.2), teal eyes, black sclera, 2 yellow v shape markings on muzzle, long brown mane, torn red cloak, extreme detail",
        "negative_prompt": "low quality, bad anatomy, text, simple horns, blue horns, armor",
        "steps": 28,
        "cfg_scale": 5.5,
        "width": 896,
        "height": 1152,
        "sampler_name": "Euler a"
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            img_data = base64.b64decode(res['images'][0])
            out_path = os.path.join(output_base, f"{name}.png")
            with open(out_path, "wb") as f:
                f.write(img_data)
            print(f"  OK: {out_path}")
    except:
        print(f"  ERR: {name}")

print("AUDIT COMPLETE.")
