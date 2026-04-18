#!/bin/bash
# --- Vilelands Forge Stabilized Launcher ---
# Resolves Python 3.12 vs 3.10 conflict and ldm module errors.

SD_DIR="/home/vile/stable-diffusion-webui"
VENV_DIR="$SD_DIR/venv"

echo "🚀 Stabilizing Environment..."

# 1. Force the correct Python path (3.10 inside the venv)
export PYTHON="$VENV_DIR/bin/python3.10"

# 2. Fix for bitsandbytes/CUDA 13 pathing (from webui-user.sh)
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$VENV_DIR/lib/python3.10/site-packages/nvidia/nvjitlink/lib"

# 3. Activation check
if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Error: venv not found at $VENV_DIR"
    exit 1
fi

source "$VENV_DIR/bin/activate"

# 4. Launch Args (Optimized for Vile Project)
# Added --skip-python-version-check to bypass the 3.12 warning if it persists
export COMMANDLINE_ARGS="--listen --api --opt-sdp-attention --no-half-vae --disable-xformers --skip-python-version-check"

echo "✨ Launching Forge (V5 Ready)..."
cd "$SD_DIR"
./webui.sh
