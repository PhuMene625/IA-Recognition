# Intelligence artificielle

## Table des matières

- [Intelligence artificielle](#intelligence-artificielle)
  - [Table des matières](#table-des-matières)
  - [Introduction](#introduction)
    - [Clone-moi !](#clone-moi-)
    - [Langage de programmation](#langage-de-programmation)
    - [Interface de développement](#interface-de-développement)
  - [Installation des bibliothèques](#installation-des-bibliothèques)
    - [Pourquoi faire ?](#pourquoi-faire-)
    - [Qu'avons-nous besoin ?](#quavons-nous-besoin-)
  - [Avant de commencer](#avant-de-commencer)
    - [Documentation](#documentation)
    - [Émulateur](#émulateur)
  - [Les bases](#les-bases)
    - [Décollage iminent](#décollage-iminent)
    - [Obtenir les coordonnées des deux écrans](#obtenir-les-coordonnées-des-deux-écrans)
      - [Grattons un peu sur le papier avant de commencer](#grattons-un-peu-sur-le-papier-avant-de-commencer)
      - [Passons au code](#passons-au-code)
    - [Capturer les deux écrans de l'émulateur](#capturer-les-deux-écrans-de-lémulateur)
      - [Quelle fonction utiliser](#quelle-fonction-utiliser)
      - [C'est parti](#cest-parti)
    - [Observer et reconnaître les personnages](#observer-et-reconnaître-les-personnages)
      - [Quelque-chose ne va pas](#quelque-chose-ne-va-pas)
      - [Qu'est-ce que l'on entend par là](#quest-ce-que-lon-entend-par-là)
      - [Corrigons ce problème là](#corrigons-ce-problème-là)
      - [Allons trouver ce personnage pour lui botter sa cible](#allons-trouver-ce-personnage-pour-lui-botter-sa-cible)
  - [Aller plus loin](#aller-plus-loin)

## Introduction

![](/doc/img/nintendo_ds.jpg)

> On a tous joué au moins une fois dans notre vie à Super Mario Bros, non ?

Pas de panique ! On ne va pas pas faire une intelligence artificielle capable
de jouer aux différents niveaux de Super Mario Bros sur la Nintendo DS 🫠

Non, on va faire une intelligence artificielle capable de jouer... à un
**mini-jeu** de Super Mario Bros !

![](/doc/img/smb_mini_games_selected.png)

Plus spécifiquement, on va s'attarder à créer quelque-chose capable d'aller le
plus loin possible au mini-jeu du « Wanted », où le but est de trouver l'image
correspondante à celle recherchée plus haut sur la partie supérieure de
l'écran 👍 

![](/doc/img/smb_mini_game_gameplay.png)

Allez, c'est parti !

### Clone-moi !

La toute première chose que l'on va te demander, c'est de cloner ce dépôt. En
réalisant cette opération, tu vas te procurer l'ensemble des fichiers présents
sur ce dernier, dont les scripts et les images nécessaires pour l'activité.

Ainsi, pas besoin de préparer le terrain au niveau du code -- on s'est déjà
occupé de ça pour que tu ais (presque) tout ce qu'il faut pour démarrer tout
de suite ! 👌

### Langage de programmation

Il existe une multitude de langages de programmation qui nous permettrait
d'accomplir la tâche d'aujourd'hui.

Cependant, un en particulier est extrêmement utilisé notamment dans le domaine
de l'intelligence artificielle de par sa simplicité d'utilisation, et en
conséquence du temps réduit en développement pour réaliser des projets.

Oui, nous parlons bien de Python ! 🐍

<!-- TODO: Plus tard, faire une introduction au langage si nécessaire -->

### Interface de développement

Tout d'abord, nous aurons besoin d'un Environnement de Développement Intégré
(EDI, en anglais *IDE*). Comme son nom l'indique, il permet d'amener un ensemble
d'outils nécessaire au développement et au test de programmes 🧪

Nous n'imposerons pas un environnement de développement en particulier, donc
tu peux très bien utiliser celui que tu souhaites si tu as déjà essayé, ou bien
même si tu as déjà réalisé des programmes auparavant.

Si tu n'as pas de préférence, ou si tu n'as jamais utilisé ce genre d'outils
auparavant, alors nous te recommandons d'utiliser
**Visual Studio Code** en le téléchargeant
[ici](https://code.visualstudio.com/) !

## Installation des bibliothèques

### Pourquoi faire ?

Pour réaliser ton intelligence artificielle, il te faudra posséder des outils
qui te permettront de faire des actions de souris, de capturer l'écran sur une
zone donnée, de repérer une image dans une autre image, etc.

Ces outils sont appelés des bibliothèques. Ce sont des « boîtes » contenant du
code réalisé par des développeurs pour faciliter et accélérer le développement
d'applications, de jeux vidéos, et plein d'autres types de programmes.

![](/doc/img/library_representation.jpg)

> Les boîtes en carton sont potentiellement vivantes et dôtés de raison.
> Fais donc attention à ce que tu fais à présent. 🥡

### Qu'avons-nous besoin ?

Dans cette activité, nous aurons besoin des bibliothèques suivantes :

- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/), une bibliothèque
  permettant de contrôler les déplacements de souris, l'entrée utilisateur, etc.
- [Pillow](https://pillow.readthedocs.io/en/stable/), une bibliothèque de
  traitement d'images.
- [OpenCV](https://opencv.org), une bibliothèque de reconnaissance d'images et
  d'intelligence artificielle.

Selon l'environnement de développement que tu as choisi, la méthode pour
installer ces différentes bibliothèques sera légèrement différente.

[Clique ici](/install.md) pour en savoir plus sur comment installer les
bibliothèques selon l'outil que tu utiliseras dans cette activité.

Il se peut aussi que les bibliothèques soient déjà installé. Une bonne façon de
vérifier ça est de lancer le script `tools/test_install.py` depuis un terminal
ou un environnement de développement intégré, et de voir si ce dernier affiche
une erreur.

Si ce n'est pas le cas, tu peux directement passer à la section
[Les bases](#les-bases).

## Avant de commencer

### Documentation

Avant de commencer, nous te conseillons fortement d'ouvrir la documentation de
[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) et
[Pillow](https://pillow.readthedocs.io/en/stable/) dans ton navigateur préféré
et de le garder quelque part tout au long de cette activité. 📘

Ces deux sites expliquent directement comment intéragir directement avec ces
fameuses « boîtes » pour parvenir à l'issue de cette activité, et notamment
comment utiliser les fonctions implémentées par ces dernières. Utile lorsque
l'on débute !

Nous te rappelons aussi que si tu es bloqué quelque-part, n'hésite surtout pas
à demander de l'aide à tes voisins, tes professeurs et les intervenants -- il
est tout à fait normal de patiner. De plus, on apprend mieux quand on se trompe,
donc tu n'as rien à perdre 😉

### Émulateur

Bien évidemment, on n'a pas de Nintendo DS à portée de main. Mais on a...
Internet ! 🌐 Et comme on vit dans un monde futuriste, on a droit à des
émulateurs en **ligne** -- ce qui fait que tu as rien à installer de plus ! 😎

Rend-toi sur [ce lien](https://www.smbgames.be/new-super-mario-bros.php) et
clique sur le bouton « Play now » pour lancer directement le jeu Super Mario
Bros depuis ton navigateur.

À partir de là, tu n'as qu'à cliquer sur les boutons « Minigames »,
« 1 player », « Puzzles » et l'icône où « Wanted » est inscrit. Tu peux faire
une voir plusieurs parties pour voir comment cela fonctionne, bien évidemment !
🕹️

Une fois que tout est prêt, on peut démarrer !

## Les bases

### Décollage iminent

![](/doc/img/ariane_liftoff.jpg)

Nous allons **enfin** pouvoir commencer à programmer ! Tu peux désormais ouvrir
le fichier [`main.py`](/main.py#L1) présent à la racine de ce dépôt.

Pour cette activité, il y a plusieurs objectifs à réaliser :

1. **Obtenir les coordonnées des deux écrans de l'émulateur en fonction de
   l'écran physique**

   Étant donné que ton écran est réellement constitué d'un ensemble de fenêtres
   qui contiennent eux-mêmes des images, des sous-fenêtres, des onglets, ou des
   écrans virtuels... il va falloir dire où est-ce que ces écrans sont situés
   par rapport à ton écran physique. 🖥️

2. **Capturer les deux écrans indépendamment, en fonction d'un paramètre**
   
   Pour que l'intelligence artificielle puisse « voir », il faut capturer la
   zone déterminée précédemment à des intervales réguliers pour bien réagir en
   fonction de l'état du jeu. 🎮

3. **Observer et reconnaître les personnages à partir d'une banque d'images**

   Nous avons besoin de savoir sur quel personnage cliquer, donc il faut que
   notre intelligence artificielle puisse identifier quel personnage est
   « Wanted » en premier lieu ! Nous avons prévu le coup, toutes les images sont
   situés dans le dossier `assets` (merci Maya ! 😜)

Il y a donc pas mal de choses à faire, mais tout est réalisable -- on espère en
tout cas que tu prendras plaisir à programmer cette fameuse intelligence
artificielle 😄 -- bon courage à toi et *have fun* !

### Obtenir les coordonnées des deux écrans

#### Grattons un peu sur le papier avant de commencer

Le premier objectif est d'obtenir les coordonnées des deux écrans virtuels,
selon les coordonnées dit « physiques ».

![](/doc/img/nintendo_ds_layout.jpg)

Pour t'aider à comprendre le principe, on va prendre exemple sur un écran
imaginaire :
```
           (0, 0)
         | ............ (12, 0)
         | ............
5 lignes | .....##.....
   (y)   | .....##.....
         v ............ (12, 4)
           ----------->
           13 colonnes
               (x)
```

Selon toi, quel serait la position du carré représenté par les « `#` » ?

- On n'attend qu'une réponse de type $(c_x, c_y)$
- Par exemple, si le carré était situé à la 4<sup>ème</sup> colonne et la
  3<sup>ème</sup> ligne de l'écran ci-dessous, on noterait donc que le carré est
  en $(4, 3)$
  ```
             (0, 0)
           | ............ (12, 0)
           | ............
  5 lignes | ............
     (y)   | ....xx......
           v ....xx...... (12, 4)
             ----------->
             13 colonnes
                 (x)
  ```
- La position du carré est donc matérialisé par le point le plus proche des
  axes (c'est à dire les flèches qui indiquent dans quel sens compter le nombre
  de lignes et de colonnes dans nos schémas)
<details>
  <summary>Voir la solution</summary>
  Alors, tu as trouvé la solution ? C'était $(5, 3)$ !
  
  Si tu n'as pas trouvé tout de suite, ou que tu as une mauvaise réponse, pas
  de panique -- demande à tes voisins ou à un encadrant de t'expliquer le
  raisonnement derrière ceci !
</details>

Bien, nous avons la position de ce carré (ou de ce rectangle plutôt), mais on
ne sait pas encore la taille de ce dernier 📏

Pour pallier à ce problème, on n'a juste qu'à ajouter deux éléments à notre...
euh.. comment ça s'appelle déjà ça ? 🤔

$(a, b, ...)$

Ah oui, ici on parle bien de **tuples** ! Et plus spécifiquement :
- d'un **couple** pour un tuple $(a, b)$
- d'un **triplet** pour un tuple $(a, b, c)$
- d'un **quadruplet** pour un tuple $(a, b, c, d)$
- et d'autres noms relativement étranges
  [que l'on peut connaître sur cette page](https://fr.wikipedia.org/wiki/Uplet#Cas_particuliers) !

Dans ce contexte là, on va surtout utiliser des quadruplets (donc des tuples à 4
valeurs) pour représenter à la fois les coordonnées du rectangle **ainsi** que
sa taille ! 🔳

Le rectangle dont on parle ici, c'est en réalité de notre fameux écran virtuel !
Et c'est exactement ce que l'on va faire ici pour capturer les deux écrans de
l'émulateur à partir de leurs coordonnés ! 🤖

#### Passons au code

[Clique ici](/main.py#L5) pour aller à l'endroit du code à modifier si tu es
sur un éditeur compatible (comme Visual Studio Code ou Replit)

Si tu as bien compris le principe, alors l'application devrait être relativement
rapide à mettre en place. 

> **CONSEIL** : On te recommande fortement d'utiliser le petit script localisé 
> dans `tools/mouse_info.py`, il te permettra rapidement d'obtenir précisément
> les coordonnées de chaque écran de l'émulateur, relatif à ton écran physique !

Ton objectif est d'implémenter la fonction `get_screen_coordinates` qui permet
d'obtenir, selon le « type » d'écran souhaité (`bottom` pour inférieur, et
`top` pour supérieur), un rectangle représenté par un quadruplet de cette
façon là :

$(s_x, s_y, s_w, s_h)$

où
- $s_x$ et $s_y$ sont donc les coordonnées du point situant l'écran
- $s_w$ et $s_h$ sont respectivement la longueur et la largeur de l'écran

> **À NOTER** : Si tu as correctement déterminé la localisation des deux écrans
> virtuels, tu devrais remarquer que :
> 
> - leur position en $s_x$ sont égaux (par exemple, tu pourrais obtenir
>   $(200, 200, 300, 300)$ et $(200, 500, 300, 300)$ )
> - leur tailles de rectangle $s_w$ et $s_h$ respectives sont égaux (ici, la
>   taille des deux écrans font $300$)
>
> Si ce n'est pas exactement le cas, tu peux très bien ajuster toi-même la
> position manuellement après coup -- il n'est pas non plus nécessaire d'obtenir
> des coordonnées parfaites.

> **LE SAIS-TU** : Le mot clé `pass` en Python permet d'indiquer à
> l'interpréteur que l'on souhaite volontairement définir un bloc de code vide.

### Capturer les deux écrans de l'émulateur

#### Quelle fonction utiliser

![](/doc/img/screen_shot.png)

[Clique ici](/main.py#L22) pour aller à l'endroit du code à modifier si tu es
sur un éditeur compatible (comme Visual Studio Code ou Replit)

Maintenant que nous avons les coordonnées de chaque écran, on peut passer à la
capture de ces dernières. Comme on l'a mentionné précédemment, les deux captures
te permettra de donner des yeux à ton IA ; de sorte à ce qu'elle puisse
identifier le personnage et sa cible ! 👓

C'est à partir de là que l'on peut faire un tour sur la documentation de
[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/). Selon-toi, quelle
fonction serait utile dans notre cas précis ? 📕

> **INDICE** : Regarde du côté de la barre latérale à gauche 🔍

<details>
  <summary>Voir la solution</summary>
  Alors, tu as trouvé ? C'est bien la fonction `screenshot` ! 📸

  Attention à ne pas capturer l'entièreté de ton écran, mais bien une **région**
  de cette dernière ! 💡

  *psst... regarde la documentation de PyAutoGUI...*
</details>

#### C'est parti

Tu as maintenat tous les outils en main, il reste plus qu'à implémenter la
fonction `get_screen_shot` qui doit **retourner** (soit `return`) une image
correspondant à une capture de l'écran donné ! Bonne chance à toi ! 🫡

> **CONSEIL** : Tu peux voir la capture d'écran réalisé avec la fonction `show`
> de l'objet. Par exemple, si tu sauvegardes ta capture d'écran dans une
> variable nommé `screen_shot`, tu peux l'afficher de cette manière là :
>
> ```py
> screen_shot.show()
> ```

### Observer et reconnaître les personnages

![](/doc/img/sherlock_searching.jpg)

[Clique ici](/main.py#L34) pour aller à l'endroit du code à modifier si tu es
sur un éditeur compatible (comme Visual Studio Code ou Replit)

Tout d'abord, bravo ! Tu as accompli une bonne partie de l'activité -- sois donc
fier de ce que tu as fait à présent 😄

Nous sommes donc maintenant à la recherche du personnage et de sa cible ! Pour
se faire, on va devoir utiliser une fonction de PyAutoGUI pour :
- **localiser** le personnage sur l'écran supérieur, et donc savoir si c'est
  celui auquel il faudra rechercher sa cible correspondante
- **localiser** la cible sur l'écran inférieur

On a été très sympa, on s'occupe déjà de tester chaque personnage et de cliquer directement sur la cible si elle est trouvé par la fonction `find_character`...
que tu as d'ailleurs à implémenter !

> **CONSEIL** : On ne répètera jamais assez, mais fais un petit tour sur la
> documentation de PyAutoGUI, tes réponses sont probablement cachés là dedans !
> 🧞

<details>
  <summary>Voir la solution</summary>
  Si tu as bien cherché, tu as alors bien trouvé la fonction `locate` (d'où le
  fait que l'on a mis en gras le terme 😜)
</details>

Bien, tu as maintenant tout ce qui te faut réaliser la fonction
`find_character`, mais... il y a un hic. 🫢

#### Quelque-chose ne va pas

Tu te rappelles que l'on a défini des **quadruplets** pour localiser les deux
écrans de l'émulateur par rapport à ton écran physique ? Quelle **taille** as-tu
stocké à la 3<sup>ème</sup> et 4<sup>ème</sup> place de ces derniers ? 

Si, par pur chance, tu as des rectangles de $256$ par $192$, eh bien je te
recommande de jouer au loto et de sauter
[ici](#allons-trouver-ce-personnage-pour-lui-botter-sa-cible). Sinon, tu fais
parti de l'écrasante majorité de personnes qui possèdent des écrans virtuels
légèrement plus grand que la « réalité ».

#### Qu'est-ce que l'on entend par là

![](/doc/img/nintendo_ds_dimensions.png)

Un écran de Nintendo DS fait exactement du $256$ par $192$ pixels, qu'il soit
supérieur ou inférieur.

Or, nous avons ici des écrans virtuels qui sont plus grand que ça -- et vu que
nous avons des images qui suivent ces dimensions de la vraie Nintendo DS. 🖥️

Nous avons donc à **redimensionner** préalablement les captures d'écran avant
de les utiliser pour identifier le personnage et sa cible correspondante !

#### Corrigons ce problème là

Encore une fois, on a pensé à tout. Une fonction `scale_screen_shot`, prenant en
paramètre une capture d'écran et qui retourne elle-même cette dernière, mais
**aux propres dimensions** a été réalisé par nos soins ! Franchement, elle est
pas belle la vie ? 😎

Tu n'as donc qu'à modifier la fonction `get_screen_shot` que tu as réalisé
précédemment pour appliquer cette correcton avant de **retourner** cette
dernière. Bonne chance ! 🧪

#### Allons trouver ce personnage pour lui botter sa cible

Ça y est, on est au cœur de notre intelligence artificielle ! 🎆

Nous n'avons plus qu'à vérifier si la tête donnée correspond à celle attendue
par la fonction `find_character` sur l'écran supérieur, et de trouver la cible
donnée sur l'écran inférieur.

Et voilà, si tu as correctement suivi le déroulé de l'activité, tu devrais avoir
une intelligence artificielle qui gagne quelques points au mini-jeu ! Bravo à
toi ! 😄

## Aller plus loin

![](/doc/img/go_beyond_the_initial_goal.webp)

Alors, combien de points as-tu obtenu avec ton intelligence artificielle ? 😛

Tu auras très certainement remarqué que plus tu avances dans les niveaux, et
plus il sera compliqué de trouver les personnages -- au point-même où toi-même
aura des difficultés à les décerner ! 🧐

Voici donc quelques pistes pour t'aider à améliorer ton intelligence
artificielle :

- **Tu peux essayer de gérer les cibles qui se déplacent en tant réel**

  Une façon de résoudre ce problème est de prendre deux captures d'écran à deux
  intervales différentes, et de calculer la trajectoire du point pour trouver la
  position réelle de la cible qui se déplace ! 🎯

- **Tu peux essayer d'améliorer la recherche des cibles**

  Comme on l'a dit, il y aura certains cas où des cibles se superposent sur
  d'autres -- ce qui rend ton intelligence artificielle « aveugle » car elle
  pense ne pas les voir. 👀
  
  Tu pourrais par exemple segmenter chaque cible individuelle en plusieurs
  petites parties et rechercher individuellement ces dernières. 🔍

- **Tu peux essayer de changer le taux de confiance pour l'identification des
  cibles**

  Tu pourrais réduire ou augmenter le taux de confiance et observer les
  cibles qui sont cliquées. Attention à ne pas trop augmenter ou réduire le
  niveau de confiance ! 🤝

- **Tu peux essayer de reconnaître la cible à partir de sa couleur**

  Au lieu de s'efforcer à identifier les cibles, pourquoi ne pas tout simplement
  tenter d'obtenir la couleur de cette dernière ? 🪣

- **Tu peux essayer de réaliser une intelligence artificielle sur un autre
  mini-jeu**

  Pourquoi ne pas tenter de réappliquer ce que tu as vu ici sur un autre
  mini-jeu ? Il y en a beaucoup de proposés, donc libre à toi de faire une autre
  intelligence artificielle adapté pour le mini-jeu que tu souhaites ! 🛝

Bien évidemment, libre à toi de proposer d'autres solutions si tu en trouves,
on ne dresse ici qu'une liste de possibités d'exploration ! 🗺️
