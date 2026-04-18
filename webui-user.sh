#!/bin/bash
# --- Vilelands Forge Configuration ---
venv_dir="venv"

# 1. Fix for bitsandbytes/CUDA 13 pathing
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/stable-diffusion-webui/venv/lib/python3.10/site-packages/nvidia/nvjitlink/lib"

# 2. Stable Args: Removed --skip-install once to let it verify the Golden Triangle
export COMMANDLINE_ARGS="--listen --api --opt-sdp-attention --no-half-vae --disable-xformers"

export NO_TCMALLOC="True"
# --- End Configuration ---
