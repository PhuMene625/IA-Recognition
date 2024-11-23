# Cette ligne est très importante, et permet d'accéder à des fonctions
# préfabriqués que l'on a fait par nos soins !
from util import *

def get_screen_coordinates(screen: str) -> tuple[int, int, int, int]:
    """
    Obtient les coordonnés de l'écran `screen`, qui peut-être :
    - `top`, pour l'écran supérieur
    - `bottom`, pour l'écran inférieur
    et le renvoit sous la forme `tuple[int, int, int, int]`
    """
    if screen == "top":
        # TODO: **Retourner** les coordonnés de l'écran supérieur, relatif à ton écran
        return (599,0,720,539)
    elif screen == "bottom":
        # TODO: **Retourner** les coordonnés de l'écran inférieur, relatif à ton écran
        return(599,539,720,539)
    else:
        # Si la demande est invalide, on renvoit une erreur explicative
        raise ValueError(f"Type d'écran '{screen}' invalide !")

def get_screen_shot(screen: str) -> Image:
    """
    Prend une capture de l'écran `screen`, qui peut-être :
    - `top`, pour l'écran supérieur
    - `bottom`, pour l'écran inférieur
    et renvoit une `Image`
    """
    coordinates = get_screen_coordinates(screen)
    # TOace: ImageDO: Prendre une capture d'écran à partir des coordonnés à l'aide de
    #       la bibliothèque PyAutoGUI et la renvoyer
    screen_shot = pyautogui.screenshot(region=coordinates)
    return screen_shot

def find_character(
        f, target: Image,
        top_screen_shot: Image, bottom_screen_shot: Image
    ) -> None | tuple[int, int, int, int]:
    """
    Recherche la tête `face` (une image correspondant à la tête du personnage en
    grand, affiché sur la partie supérieure de l'écran) depuis la capture
    d'écran `screen_shot` et renvoie
    - `None` si aucun personnage n'a été trouvé
    - `tuple[int, int, int, int]` désignant les coordonnées de la cible à
      cliquer, ainsi que sa taille en longueur et en largeur
    """
    # TODO: Localiser la tête `face` du personnage dans l'image
    #       `top_screen_shot`.
    #       Dans le cas où la tête a été trouvé, localiser la cible `target`
    #       dans l'image `bottom_screen_shot`
    #       Sinon, retourner `None`.
    top = scale_screen_shot(top_screen_shot)
    bottom = scale_screen_shot(bottom_screen_shot)

    # TODO: Localiser la tête `face` du personnage dans l'image
    #       `top_screen_shot`.
    #       Dans le cas où la tête a été trouvé, localiser la cible `target`
    #       dans l'image `bottom_screen_shot`
    #       Sinon, retourner `None`.
    try:
        pyautogui.locate(face, top, confidence=0.7)
        print("Tête Trouvée")
    except Exception:
        print("putain g pas la tete")
        return None

    try:
        target_loc = pyautogui.locate(target, bottom, confidence=0.6)
        print("target locked")
    except Exception:
        print("ptn michel je trouve pas ma cible")
        return None

    target_loc = (target_loc[0] + target.size[0] / 2, target_loc[1] + target.size[1] / 2)

    return target_loc
################################################################################
# Ce qui suit est le squelette d'exécution de ton intelligence artificielle    #
# Tu pourras modifier cette partie QU'À PARTIR de la section                   #
# « Aller plus loin »                                                          #
################################################################################

bottom_coordinates = get_screen_coordinates("bottom")

while True:
    # On obtient une capture des deux écrans de l'émulateur
    top_screen_shot = get_screen_shot("top")
    bottom_screen_shot = get_screen_shot("bottom")

    for (character, face, target) in characters:
            # On essaye de trouver un personnage
            target_position = find_character(face, target, top_screen_shot,
                                            bottom_screen_shot)
            # Si c'est le cas...
            if target_position:
                pyautogui.click(bottom_coordinates[0],bottom_coordinates[1])
                real_position = get_true_location(bottom_coordinates, target_position)
                pyautogui.move(real_position)

                break

        # On attend 1 seconde avant de recommencer l'opération
    time.sleep(1)
