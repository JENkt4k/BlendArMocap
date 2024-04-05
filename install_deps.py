import subprocess
import sys
import os
import bpy

bpy.ops.preferences.addon_enable(module='BlendArMocap')
bpy.ops.wm.save_userpref()

#path to python.exe
python_exe = os.path.join(sys.prefix, 'bin', 'python')
py_lib = os.path.join(sys.prefix, 'bin','pip')

#install opencv
subprocess.call([python_exe, py_lib, "install", "opencv_python"])
#install mediapipe
subprocess.call([python_exe, py_lib, "install", "mediapipe"])

subprocess.call([python_exe, py_lib, "install", "numpy"])


# import subprocess
# import sys

# def install_package(package):
#     subprocess.check_call([sys.executable, "-m", "ensurepip", "--user"])
#     subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])

# packages = ["opencv-python-headless", "mediapipe"]

# for pkg in packages:
#     try:
#         install_package(pkg)
#     except Exception as e:
#         print(f"Failed to install {pkg}: {str(e)}")
