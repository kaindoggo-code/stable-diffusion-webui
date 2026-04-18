import urllib.request
import json
import base64
import os
import time

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
epochs = ['ep4', 'ep6', 'ep8', 'ep10']
output_base = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/UNSTOPPABLE_AUDIT")
os.makedirs(output_base, exist_ok=True)

while True:
    try:
        urllib.request.urlopen("http://127.0.0.1:7860/")
        break
    except:
        print("Waiting for Forge...")
        time.sleep(5)

prompt = "masterpiece, amazing quality, source_furry, <lora:vilefox_v1:1.0>, vilefox, solo, male, anthro, orange fur, teal eyes, black sclera, small curved horns with teal and black stripes and golden runes, torn damaged red cloak, 04_ART style"

for ep in epochs:
    print(f"Auditing {ep}...")
    current_prompt = prompt.replace("<lora:vilefox_v1:1.0>", f"<lora:vilefox_{ep}:1.0>")
    
    for i in range(3):
        payload = {
            "prompt": current_prompt,
            "negative_prompt": "low quality, bad anatomy",
            "steps": 20,
            "width": 896,
            "height": 1152,
            "sampler_name": "Euler a"
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req) as response:
                res = json.loads(response.read().decode('utf-8'))
                img_data = base64.b64decode(res['images'][0])
                out_path = os.path.join(output_base, f"{ep}_test_{i+1}.png")
                with open(out_path, "wb") as f:
                    f.write(img_data)
                print(f"  OK: {out_path}")
        except:
            print(f"  ERR: {ep} batch {i+1}")

print("AUDIT FINISHED.")
