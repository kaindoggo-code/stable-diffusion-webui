import urllib.request
import json
import base64
import os

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
weights = [0.7, 0.9, 1.1]
cfgs = [4.5, 6.0]
styles = ["monochrome ink sketch", "vibrant high-detail digital art"]

output_base = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/SHOTGUN")
os.makedirs(output_base, exist_ok=True)

print("SHOTGUN EXPERIMENT STARTING...")

for w in weights:
    for c in cfgs:
        for s in styles:
            name = f"weight{w}_cfg{c}_{s.replace(' ', '_')}"
            print(f"Firing {name}...")
            payload = {
                "prompt": f"masterpiece, amazing quality, <lora:vilefox_v1:{w}>, vilefox, solo, male, anthro, {s}, orange fur, white muzzle, teal eyes, black sclera, black tendril tongue, blue saliva, striped horns, golden runes, torn red cloak, extreme detail",
                "negative_prompt": "low quality, bad anatomy, text, human, female",
                "steps": 24,
                "cfg_scale": c,
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

print("SHOTGUN COMPLETE.")
