# 2025 Copyright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = os.path.join(BASE_DIR, "venv", "Scripts", "python.exe")
FRACTURE = os.path.join(BASE_DIR, "fracture.py")

if len(sys.argv) < 2:
    input("Aucun fichier .ftr fourni.")
    sys.exit(1)

subprocess.call([PYTHON, FRACTURE, sys.argv[1]])



# pyinstaller --onefile --noconsole fracture_launcher.py
