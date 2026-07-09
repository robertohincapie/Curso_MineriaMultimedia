import shutil
import subprocess
import sys

GPU_INDEX = "https://download.pytorch.org/whl/cu124"

def tiene_nvidia():
    return shutil.which("nvidia-smi") is not None

print("Sincronizando dependencias...")
subprocess.run(["uv", "sync"], check=True)

if tiene_nvidia():
    print("GPU NVIDIA detectada.")
    subprocess.run([
        "uv",
        "add",
        "torch",
        "torchvision",
        "torchaudio",
        "--index",
        GPU_INDEX
    ], check=True)
else:
    print("Instalando versión CPU.")
    subprocess.run([
        "uv",
        "add",
        "torch",
        "torchvision",
        "torchaudio"
    ], check=True)