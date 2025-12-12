# Copryright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

import os
import subprocess
import sys


def main():
    # Dossier où se trouve fracture_launcher.exe
    base = os.path.dirname(os.path.abspath(sys.executable))

    # Python portable embarqué
    python_embedded = os.path.join(base, "FracturePython", "python.exe")

    # Script principal de Fracture
    script = os.path.join(base, "fracture.py")

    # Vérifications
    if not os.path.isfile(python_embedded):
        raise FileNotFoundError(f"Python portable introuvable : {python_embedded}")

    if not os.path.isfile(script):
        raise FileNotFoundError(f"Script fracture.py introuvable : {script}")

    # Commande finale : python.exe fracture.py <arguments>
    cmd = [python_embedded, script] + sys.argv[1:]

    # Lancer fracture.py avec le Python portable
    subprocess.call(cmd)


if __name__ == "__main__":
    main()


# pyinstaller --onefile --noconsole fracture_launcher.py
