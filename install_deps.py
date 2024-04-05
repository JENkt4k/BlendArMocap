import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "ensurepip", "--user"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])

packages = ["opencv-python-headless", "mediapipe"]

for pkg in packages:
    try:
        install_package(pkg)
    except Exception as e:
        print(f"Failed to install {pkg}: {str(e)}")
