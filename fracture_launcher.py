# 2025 Copyright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

import os
import subprocess
import sys

def main():
    base = os.path.dirname(os.path.abspath(sys.executable))
    python_embedded = os.path.join(base, "FracturePython", "python.exe")
    script = os.path.join(base, "fracture.py")

    # Vérifications
    if not os.path.isfile(python_embedded):
        print(f"Python portable introuvable : {python_embedded}")
        input("Appuyez sur ENTRÉE pour fermer...")
        return

    if not os.path.isfile(script):
        print(f"Script fracture.py introuvable : {script}")
        input("Appuyez sur ENTRÉE pour fermer...")
        return

    # Construire la commande avec tous les arguments
    args = " ".join(f'"{arg}"' for arg in sys.argv[1:])
    cmd = f'"{python_embedded}" "{script}" {args}'

    # Exécuter fracture.py et garder la console ouverte si double-clic
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    main()


# pyinstaller --onefile --noconsole fracture_launcher.py
