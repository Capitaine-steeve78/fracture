# Copryright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

import os
import subprocess
import sys


def main():
    # Dossier où se trouve fracture_launcher.exe
    base = os.path.dirname(os.path.abspath(sys.executable))

    # Python du venv
    python_venv = os.path.join(base, "FractureEnv", "Scripts", "python.exe")

    # Script principal
    script = os.path.join(base, "fracture.py")

    # Vérifications
    if not os.path.isfile(python_venv):
        raise FileNotFoundError(f"Python du venv introuvable : {python_venv}")

    if not os.path.isfile(script):
        raise FileNotFoundError(f"Script fracture.py introuvable : {script}")

    # Commande finale
    cmd = [python_venv, script] + sys.argv[1:]

    # Lancer fracture.py dans le venv
    subprocess.call(cmd)


if __name__ == "__main__":
    main()

# pyinstaller --onefile --noconsole fracture_launcher.py
