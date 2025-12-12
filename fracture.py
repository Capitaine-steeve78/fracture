# Copyright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

# pyinstaller --onefile --icon=fracture-logo.ico fracture.py
# python.exe fracture.py test.ftr

import ast
import importlib
import os
import subprocess
import sys
import types

from rich.console import Console

console_rich = Console()

# ---------------------------------------------------------------------------
#  BASE_DIR = dossier du script ou dossier temporaire PyInstaller (_MEIPASS)
# ---------------------------------------------------------------------------
BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

MODULES_DIR = os.path.join(BASE_DIR, "modules")

# ---------------------------------------------------------------------------
#  Trouver python portable intégré dans FracturePython/
# ---------------------------------------------------------------------------
def get_embedded_python():
    return os.path.join(BASE_DIR, "FracturePython", "python.exe")

EMBEDDED_PYTHON = get_embedded_python()

# ---------------------------------------------------------------------------
#  Ajouter site-packages du Python portable au sys.path
# ---------------------------------------------------------------------------
def patch_sys_path_for_embedded_python():
    site = os.path.join(BASE_DIR, "FracturePython", "Lib", "site-packages")
    if os.path.isdir(site) and site not in sys.path:
        sys.path.insert(0, site)

patch_sys_path_for_embedded_python()

# Stockage des modules chargés
modules_loaded = {}
variables = {}

# ---------------------------------------------------------------------------
#  Installation automatique des modules Python manquants (dans Python portable)
# ---------------------------------------------------------------------------
def require_python_module(module_name):
    try:
        importlib.import_module(module_name)
        return True

    except ImportError:
        console_rich.print(f"[yellow]Dépendance Python '{module_name}' manquante → installation...[/yellow]")

        try:
            subprocess.check_call([EMBEDDED_PYTHON, "-m", "pip", "install", module_name, "-t",
                                   os.path.join(BASE_DIR, "FracturePython", "Lib", "site-packages")])
            console_rich.print(f"[green]Module '{module_name}' installé dans Python portable.[/green]")
            return True

        except subprocess.CalledProcessError as e:
            console_rich.print(f"[red]Échec de l'installation du module '{module_name}' : {e}[/red]")
            return False

# ---------------------------------------------------------------------------
#  Analyse AST pour détecter les imports Python dans un module Fracture
# ---------------------------------------------------------------------------
def import_dependencies(module_path):
    if not os.path.isfile(module_path):
        return

    with open(module_path, "r", encoding="utf-8") as file_handle_ast:
        tree = ast.parse(file_handle_ast.read(), filename=module_path)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                require_python_module(n.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            require_python_module(node.module)

# ---------------------------------------------------------------------------
#  Charger un module Fracture : modules/<nom>/<nom>.py
# ---------------------------------------------------------------------------
def load_module(name):
    module_dir = os.path.join(MODULES_DIR, name)
    module_path = os.path.join(module_dir, f"{name}.py")

    if not os.path.isfile(module_path):
        console_rich.print(f"[red]Module '{name}' introuvable : {module_path}[/red]")
        return

    import_dependencies(module_path)

    module = types.ModuleType(name)
    with open(module_path, "r", encoding="utf-8") as fh:
        code = fh.read()

    try:
        exec(code, module.__dict__)
    except (SyntaxError, NameError, AttributeError, TypeError) as e:
        console_rich.print(f"[red]Erreur dans le module '{name}' : {e}[/red]")
        return

    modules_loaded[name] = module

# ---------------------------------------------------------------------------
#  Résoudre module.attr1.attr2
# ---------------------------------------------------------------------------
def resolve_path(path):
    parts = path.split(".")

    if parts[0] in modules_loaded:
        obj = modules_loaded[parts[0]]
    elif parts[0] in variables:
        obj = variables[parts[0]]
    else:
        raise ValueError(f"'{parts[0]}' n'est ni un module ni une variable.")

    for part in parts[1:]:
        if hasattr(obj, part):
            obj = getattr(obj, part)
        else:
            raise AttributeError(f"'{type(obj).__name__}' n'a pas d'attribut '{part}'.")

    return obj

# ---------------------------------------------------------------------------
#  Exécuter une ligne .ftr
# ---------------------------------------------------------------------------
def execute_line(line_text):
    line = line_text.strip()

    if not line or line.startswith("#"):
        return

    if line.startswith("use "):
        module_name = line[4:].strip()
        load_module(module_name)
        return

    if "logic" in modules_loaded and getattr(modules_loaded["logic"], "logic").skip:
        if not line.startswith("logic."):
            return

    if "=" in line:
        var_name, value = map(str.strip, line.split("=", 1))

        if value.startswith('"') and value.endswith('"'):
            variables[var_name] = value[1:-1]
        else:
            try:
                variables[var_name] = resolve_path(value)
            except (ValueError, AttributeError):
                variables[var_name] = value
        return

    try:
        if "(" in line and line.endswith(")"):
            call_part = line[:line.index("(")]
            args_part = line[line.index("(") + 1:-1]
        else:
            call_part = line
            args_part = ""

        obj = resolve_path(call_part)

        if args_part.startswith('"') and args_part.endswith('"'):
            arg = args_part[1:-1]
            if callable(obj): obj(arg)
        elif args_part:
            arg = variables.get(args_part, args_part)
            if callable(obj): obj(arg)
        else:
            if callable(obj): obj()

    except (ValueError, AttributeError, TypeError) as e:
        console_rich.print(f"[red]Erreur : {e}[/red]")

# ---------------------------------------------------------------------------
#  Programme principal
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        console_rich.print("[yellow]Usage : fracture.exe fichier.ftr[/yellow]")
        sys.exit(1)

    ftr_file = sys.argv[1]

    if not os.path.isfile(ftr_file):
        console_rich.print(f"[red]Fichier '{ftr_file}' introuvable.[/red]")
        sys.exit(1)

    with open(ftr_file, "r", encoding="utf-8") as file_handle_main:
        lines = file_handle_main.readlines()

    for l in lines:
        execute_line(l)
