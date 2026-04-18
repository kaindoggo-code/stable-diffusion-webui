#!/bin/bash
# --- Vilelands Forge Master Stabilized Launcher ---
# Resolves Python 3.12 vs 3.10 conflict, Gradio 1404 KeyError, and VRAM chokes.

SD_DIR="/home/vile/stable-diffusion-webui"
VENV_DIR="$SD_DIR/venv"

echo "🚀 Stabilizing Environment (Vilefox V5 Elite Mode)..."

# 1. Force the correct Python path (3.10 inside the venv)
export PYTHON="$VENV_DIR/bin/python3.10"

# 2. Fix for bitsandbytes/CUDA 13 pathing
export LD_LIBRARY_PATH="$VENV_DIR/lib/python3.10/site-packages/nvidia/nvjitlink/lib:$VENV_DIR/lib/python3.10/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH"

# 3. Memory & Stability Fixes
export NO_TCMALLOC="True"
export GRADIO_ANALYTICS_ENABLED=False
export GRADIO_SERVER_NAME="0.0.0.0"

# 4. Activation check
if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Error: venv not found at $VENV_DIR"
    exit 1
fi

source "$VENV_DIR/bin/activate"

# 5. Launch Args (Optimized for Vilefox Project & RTX 3060)
# - Using Port 7862 as requested in RESTAR AN OPEN ME.txt
# - --always-offload-from-vram prevents the 91% VRAM weight lock
# - --opt-sdp-attention provides high speed without xformers conflicts
# Unset first to prevent double-args from environment
unset COMMANDLINE_ARGS
ARGS="--listen --port 7862 --api --opt-sdp-attention --no-half-vae --disable-xformers --always-offload-from-vram --skip-python-version-check"

echo "✨ Launching Forge on Port 7862 (VRAM Safe)..."
cd "$SD_DIR"
python3 launch.py $ARGS

