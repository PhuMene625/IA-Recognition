#!/usr/bin/env python3.10

import pkg_resources
import sys

required_packages = {
    "PyAutoGUI": False,
    "Pillow": False
}

shown_status = False

def print_error_status(msg: str):
    print(msg)
    shown_status = True

print("Vérification des bibliothèques : ", end='')

for package in pkg_resources.working_set:
    if package.project_name in required_packages:
        required_packages[package.project_name] = True

for package_name, present in required_packages.items():
    if not present:
        if not shown_status:
            print_error_status("vérification échouée")
        print(f"Bibliothèque `{package_name}` manquante")

if not shown_status:
    print("succès")

print("Vérification de l'installation d'OpenCV : ", end='')

try:
    import cv2
except ImportError:
    print_error_status("non installé")

if not shown_status:
    print("succès")
    print("Tu es prêt pour l'activité !")

sys.exit(int(shown_status))
