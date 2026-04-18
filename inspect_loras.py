import urllib.request
import json
import base64
import os
import time

url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
epochs = ['ep2', 'ep4', 'ep6', 'ep8', 'ep10']
output_dir = os.path.expanduser("~/Desktop/Cyrus_Faces/LORA_TESTS")
os.makedirs(output_dir, exist_ok=True)

print(f"Beginning Automated LoRA Inspection for {len(epochs)} epochs...")

for ep in epochs:
    print(f"\n[+] Testing vilefox_{ep}.safetensors...")
    payload = {
        "prompt": f"masterpiece, amazing quality, source_furry, <lora:vilefox_{ep}:1.0>, vilefox, solo, anthro, male, orange fur, white muzzle, brown hair, blue eyes, black sclera, grinning, red cloak, muscular, extreme detail, 04_ART style",
        "negative_prompt": "low quality, bad anatomy, human, text",
        "steps": 28,
        "cfg_scale": 4.5,
        "width": 1024,
        "height": 1024,
        "sampler_name": "Euler a",
        "override_settings": {
            "sd_model_checkpoint": "novaFurryXL_ilV170.safetensors"
        }
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
    
    start = time.time()
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            img_data = base64.b64decode(res['images'][0])
            
            out_path = os.path.join(output_dir, f"vilefox_{ep}_test_nova.png")
            with open(out_path, "wb") as f:
                f.write(img_data)
                
            elapsed = time.time() - start
            print(f"  -> SUCCESS: Saved {out_path} in {elapsed:.2f} seconds.")
    except Exception as e:
        print(f"  -> FAILED: {e}")

print("\nAll LoRA tests complete. Please check the LORA_TESTS folder.")
