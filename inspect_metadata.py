import json
import os

filepath = "/home/vile/stable-diffusion-webui/models/Lora/vilefox_ep10.safetensors"

with open(filepath, 'rb') as f:
    # Safetensors format has header length in the first 8 bytes
    header_size = int.from_bytes(f.read(8), 'little')
    header_json = f.read(header_size).decode('utf-8')
    header = json.loads(header_json)
    
    # Extract metadata (usually in the __metadata__ key)
    metadata = header.get("__metadata__", {})
    
    output_path = "/home/vile/Desktop/Cyrus_Faces/vilefox_lora_internal_data.txt"
    with open(output_path, "w") as out:
        out.write(json.dumps(metadata, indent=4))
    
    print(f"LoRA metadata extracted to: {output_path}")
    print("\nSAMPLE CAPTIONS FOUND IN LORA:")
    # Print the first few captions if available
    train_info = metadata.get("ss_tag_frequency", "No tags found")
    print(train_info[:1000] + "...")

