#!/bin/bash
# --- Vilelands Forge Safe Mode Launcher ---
SD_DIR="/home/vile/stable-diffusion-webui"
VENV_DIR="$SD_DIR/venv"

echo "🚀 Launching in SAFE MODE (Port 7860)..."

# 1. Essential Paths
export PYTHON="$VENV_DIR/bin/python3.10"
export LD_LIBRARY_PATH="$VENV_DIR/lib/python3.10/site-packages/nvidia/nvjitlink/lib:$VENV_DIR/lib/python3.10/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH"

# 2. Force Stability
export GRADIO_ANALYTICS_ENABLED=False
source "$VENV_DIR/bin/activate"

# 3. Safe Args
unset COMMANDLINE_ARGS
ARGS="--api --opt-sdp-attention --no-half-vae --disable-xformers --always-offload-from-vram --skip-python-version-check"

echo "✨ System ready. Open http://127.0.0.1:7860"
cd "$SD_DIR"
python3 launch.py $ARGS

