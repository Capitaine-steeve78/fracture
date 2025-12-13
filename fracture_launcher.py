# 2025 Copyright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

import sys
import os

# pour gérer PyInstaller --onefile
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS  # dossier temporaire PyInstaller
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EMBEDDED_PYTHON = os.path.join(BASE_DIR, "venv", "Scripts", "python.exe")




# pyinstaller --onefile --noconsole fracture_launcher.py

# pyinstaller --onefile --console fracture_launcher.py
