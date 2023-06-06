import os
import time
import pyautogui

from PIL.Image import Image, Resampling
from PIL.Image import open as open_image

NDS_SCREEN_SIZE = (256, 192)
"""Dimensions physique en pixels d'un écran de la Nintendo DS"""

def get_characters() -> list[tuple[str, Image, Image]]:
    """
    Charge toutes les images associés à chaque personnage, et renvoit sous forme de
    liste un ensemble de tuple sous la forme `tuple[str, Image, Image]`, contenant
    individuellement :
    - le nom du personnage (chaîne de caractères),
    - la tête du personnage en grand (une `Image`)
    - l'image cible à cliquer sur l'écran inférieur (une `Image`)
    """
    characters = []

    for name in ["luigi", "mario", "wario", "yoshi"]:
        characters.append((name, open_image(f"assets/{name}.png"), open_image(f"assets/{name}_icon.png")))
    
    return characters

characters = get_characters()


def scale_screen_shot(screen_shot: Image) -> Image:
    """
    Redimensionne la capture d'écran `screen_shot` pour obtenir un ratio visuel
    de 1:1 par rapport à un écran physique de Nintendo DS.
    """

    return screen_shot.resize(NDS_SCREEN_SIZE, Resampling.NEAREST)

def get_true_location(screen: tuple[int, int, int, int], point: tuple[int, int]) -> tuple[int, int]:
    """
    Redimmensionne le point `point` relatif à l'écran virtuel `screen` pour
    correspondre à l'écran physique
    """
    
    return (
        screen[0] + screen[2] / NDS_SCREEN_SIZE[0] * point[0],
        screen[1] + screen[3] / NDS_SCREEN_SIZE[1] * point[1]
    )
