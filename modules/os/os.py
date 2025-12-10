# Copryright, FractureV1 By Capitaine-steeve78 official repo : https://github.com/Capitaine-steeve78/fracture

# modules/os/os.py
import sys
import time


class Console:
    @staticmethod
    def write(text):
        sys.stdout.write(text + "\n")


def os_help():
    sys.stdout.write("commande d'aide du module os \n")

class Time:
    @staticmethod
    def pause(seconds):
        time.sleep(int(seconds))


# Créer une instance globale pour que main.py puisse y accéder
console = Console()
os_time = Time()
