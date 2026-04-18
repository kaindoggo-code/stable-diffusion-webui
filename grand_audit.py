import urllib.request
import json
import base64
import os
import time

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
epochs = ['ep4', 'ep6', 'ep8', 'ep10']
output_base = os.path.expanduser("~/Desktop/Cyrus_Faces/V5_OUTPUTS/GRAND_AUDIT")
os.makedirs(output_base, exist_ok=True)

# WAIT FOR SERVER
while True:
    try:
        urllib.request.urlopen("http://127.0.0.1:7860/")
        print("FORGE SERVER DETECTED. STARTING AUDIT...")
        break
    except:
        print("Waiting for Forge to stabilize...")
        time.sleep(5)

prompt = "masterpiece, amazing quality, source_furry, <lora:vilefox_v1:1.0>, vilefox, solo, anthro, male, orange fur, white muzzle, teal eyes, black sclera, small curved horns with teal and black stripes and golden runes, torn damaged red cloak, muscular, extreme detail, 04_ART style"

for ep in epochs:
    ep_dir = os.path.join(output_base, ep)
    os.makedirs(ep_dir, exist_ok=True)
    print(f"\n[+] Auditing {ep}...")
    
    current_prompt = prompt.replace("<lora:vilefox_v1:1.0>", f"<lora:vilefox_{ep}:1.0>")
    
    payload = {
        "prompt": current_prompt,
        "negative_prompt": "low quality, bad anatomy, human, text, blue fur",
        "steps": 28,
        "cfg_scale": 5.5,
        "width": 896,
        "height": 1152,
        "sampler_name": "Euler a",
        "batch_size": 1,
        "n_iter": 10
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            for i, img_b64 in enumerate(res['images'][:10]):
                img_data = base64.b64decode(img_b64)
                out_path = os.path.join(ep_dir, f"{ep}_render_{i+1}.png")
                with open(out_path, "wb") as f:
                    f.write(img_data)
            print(f"  -> SUCCESS: Created 10 images for {ep}")
    except Exception as e:
        print(f"  -> FAILED: {e}")

print("GRAND AUDIT COMPLETE.")
