# 2025 Copyright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

import sys
import os
import subprocess
import ctypes

# -----------------------------------------------------------
# Déterminer BASE_DIR correctement selon PyInstaller ou dev
# -----------------------------------------------------------
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------
# Python intégré (venv installé dans le dossier de l'app)
# -----------------------------------------------------------
EMBEDDED_PYTHON = os.path.join(BASE_DIR, "venv", "Scripts", "python.exe")

# -----------------------------------------------------------
# Vérifier que le venv existe
# -----------------------------------------------------------
if not os.path.isfile(EMBEDDED_PYTHON):
    ctypes.windll.user32.MessageBoxW(
        0,
        "Python interne introuvable.\nRéinstalle Fracture.",
        "Fracture – erreur",
        16
    )
    sys.exit(1)

# -----------------------------------------------------------
# Vérifier les arguments
# -----------------------------------------------------------
try:
    if len(sys.argv) < 2:
        raise ValueError("Aucun fichier .ftr fourni")

    ftr_file = sys.argv[1]

    if not os.path.isfile(ftr_file):
        raise FileNotFoundError(f"Fichier '{ftr_file}' introuvable.")

except Exception as e:
    ctypes.windll.user32.MessageBoxW(
        0,
        str(e),
        "Fracture – erreur",
        16
    )
    sys.exit(1)

# -----------------------------------------------------------
# Lancer le moteur fracture.py avec le fichier .ftr
# -----------------------------------------------------------
FRACTURE_SCRIPT = os.path.join(BASE_DIR, "fracture.py")

if not os.path.isfile(FRACTURE_SCRIPT):
    ctypes.windll.user32.MessageBoxW(
        0,
        f"Le moteur '{FRACTURE_SCRIPT}' est introuvable.",
        "Fracture – erreur",
        16
    )
    sys.exit(1)

try:
    # On appelle le moteur via le venv
    subprocess.check_call([EMBEDDED_PYTHON, FRACTURE_SCRIPT, ftr_file])
except subprocess.CalledProcessError as e:
    ctypes.windll.user32.MessageBoxW(
        0,
        f"Erreur à l'exécution du moteur : {e}",
        "Fracture – erreur",
        16
    )
    sys.exit(1)





# pyinstaller --onefile --noconsole fracture_launcher.py

# pyinstaller --onefile --console fracture_launcher.py
