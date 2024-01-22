from utils.afficher_tour import afficher_tour
from utils.effacer_ecran import effacer_ecran
from utils.input import demanderEntier
from utils.couleurs import gris_foncé_re, jaune_re, rouge_clair_re, couleur_joueur
from utils.titre import centrer_couleur, séparateur_avec_titre
from scores.entrée import EntréeScore
from scores.fichier import écrireScore
from utils.est_robot import est_robot
from random import choice

def afficher_morpion(morpion : list[list[str]]) -> None:
    """
    Procédure qui affiche proprement le morpion
    
    ## Entrée :
    
    - `morpion`, une liste de listes de chaînes de caractères, qui représente le morpion.
    """
    ligne_index : int
    case_index : int
    ligne: str
    case_actuelle: str

    # On ajout un saut de ligne avant le morpion. 
    print("")

    for ligne_index in range(3):
        ligne = " "

        for case_index in range(3):
            case_actuelle = morpion[ligne_index][case_index]

            # Si la case ne contient pas "X" ou "O",
            # alors on ne l'a pas rempli.
            # On va alors la griser pour montrer qu'elle peut être
            # sélectionné avec le nombre qu'elle contient.
            if (case_actuelle != "X" and case_actuelle != "O"):
                ligne += gris_foncé_re(case_actuelle)
            # O: Joueur 1
            elif (case_actuelle == "O"):
                ligne += jaune_re(case_actuelle)
            # X: Joueur 2
            elif (case_actuelle == "X"):
                ligne += rouge_clair_re(case_actuelle)

            # On n'ajoute pas le séparateur à la fin.
            if case_index != 2:
                ligne += " │ "

        ligne += " "
        print(centrer_couleur(ligne))

        # On n'affiche pas le séparateur à la fin.
        if ligne_index != 2:
            print(centrer_couleur("───┼───┼───"))

    # On ajout un saut de ligne après le morpion. 
    print("")

def estRemplie(char: str) -> bool:
    return char in ["X", "O"]

def main_morpion(joueur1: str, joueur2: str, difficulté_robot1: str, difficulté_robot2: str) -> None:
    """
    Procédure qui sert de point d'entrée pour le lanceur.
    C'est la procédure principale du jeu morpion.

    * Le joueur 1 jouera avec "O".
    * Le joueur 2 jouera avec "X".

    ## Entrée :

    - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
    - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
    - `difficulté_robot1`, une chaîne, qui représente la difficulté du robot 1.
    - `difficulté_robot2`, une chaîne, qui représente la difficulté du robot 2.
    """

    jeu_en_cours : bool
    égalité : bool
    nb_tour : int
    morpion : list[list[str]]
    choix : int
    joueur_actuel     : str
    difficulté_actuel : str
    adversaire_actuel : str
    # Variables utilisés dans les boucles.
    ligne_index : int
    colonne_index : int
    case_index  : int
    i : int

    # variables utilisées pour les robots
    case_dispo : list[int]
    choix_possible : list[int]

    jeu_en_cours = True
    égalité      = False
    # On commence réellement au tour 1.
    # Voir la boucle `while` en dessous.
    nb_tour = 0
    # La grille initiale quand on commence le jeu.
    morpion =  [["0","1","2"],
                ["3","4","5"],
                ["6","7","8"]]
    score = EntréeScore()
    score.type_jeu = "morpion"

    case_dispo = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Au début du jeu, on est au tour 1.
    joueur_actuel     = joueur1
    adversaire_actuel = joueur2

    while jeu_en_cours:
        nb_tour += 1

        # On récupère le nom du joueur qui doit jouer.
        if nb_tour % 2 == 1:
            joueur_actuel     = joueur1
            adversaire_actuel = joueur2
            difficulté_actuel = difficulté_robot1
        else:
            joueur_actuel     = joueur2
            adversaire_actuel = joueur1
            difficulté_actuel = difficulté_robot2

        effacer_ecran()
        afficher_tour(nb_tour)
        afficher_morpion(morpion)

        # Si c'est un robot qui joue, un algorithme est donc lancé pour effectuer le tour du robot
        # sinon le joueur joue
        if est_robot(joueur_actuel):
            if difficulté_actuel == "1":
                choix = choice(case_dispo)

            else:
                choix_possible = []

                choix = choice(case_dispo)

                # Pour le premier tour du robot, il jouera forcément dans les coins
                if nb_tour == 1 or nb_tour == 2:
                    choix = choice([0, 2, 6, 8])

                # Le robot regarde toute les possibilité de gagné ou de ne pas perdre
                # choix pour les colonnes  
                for colonne_index in range(0,3):
                    if morpion[colonne_index][0] == morpion[colonne_index][1]:
                        choix_possible.append(2 + 3 * colonne_index)
                    if morpion[colonne_index][1] == morpion[colonne_index][2]:
                        choix_possible.append(0 + 3 * colonne_index)
                    if morpion[colonne_index][0] == morpion[colonne_index][2]:
                        choix_possible.append(1 + 3 * colonne_index)

                # choix pour les lignes 
                for ligne_index in range(0,3):
                    if morpion[0][ligne_index] == morpion[1][ligne_index]:
                        choix_possible.append(6 + ligne_index)
                    if morpion[1][ligne_index] == morpion[2][ligne_index]:
                        choix_possible.append(0 + ligne_index)
                    if morpion[0][ligne_index] == morpion[2][ligne_index]:
                        choix_possible.append(3 + ligne_index)

                # choix pour les diagonales 
                if morpion[0][0] == morpion[1][1]:
                    choix_possible.append(8)
                if morpion[1][1] == morpion[2][2]:
                    choix_possible.append(0)
                if morpion[2][2] == morpion[0][0]:
                    choix_possible.append(4)

                if morpion[0][2] == morpion[1][1]:
                    choix_possible.append(6)
                if morpion[2][0] == morpion[1][1]:
                    choix_possible.append(2)
                if morpion[2][0] == morpion[0][2]:
                    choix_possible.append(4)

                # Le robot élimine les cases déjà prises
                i = 0
                while i < len(choix_possible):
                    if choix_possible[i] not in case_dispo:
                        choix_possible.pop(i)
                    else:
                        i += 1

                # Test pour pas que le robot choisi une case déjà prise
                if choix_possible != []:
                    choix = choice(choix_possible)
                else:
                    choix = choice(case_dispo)

            print(couleur_joueur(joueur_actuel, joueur1, joueur2), ", a choisi la case", choix, "!")
        else:
            choix = demanderEntier(couleur_joueur(joueur_actuel, joueur1, joueur2) + ", veuillez choisir une case : ")

        # Si la case choisie n'est pas bonne, on redemande.
        while choix < 0 or choix > 8 or estRemplie(morpion[choix // 3][choix % 3]):
            choix = demanderEntier(couleur_joueur(joueur_actuel, joueur1, joueur2) + ", veuillez choisir une case valide : ")

        case_dispo.remove(int(morpion[choix // 3][choix % 3]))

        if joueur_actuel == joueur1:
            morpion[choix // 3][choix % 3] = "O"
        elif joueur_actuel == joueur2:
            morpion[choix // 3][choix % 3] = "X"

        # On vérifie la diagonale de haut-gauche à bas-droite.
        if morpion[0][0] == morpion[1][1] and morpion[0][0] == morpion[2][2] and estRemplie(morpion[0][0]):
            jeu_en_cours = False

        # On vérifie la diagonale de haut-droite à bas-gauche.
        if morpion[0][2] == morpion[1][1] and morpion[0][2] == morpion[2][0] and estRemplie(morpion[0][2]):
            jeu_en_cours = False

        # On vérifie les lignes.
        for ligne_index in range(3):
            if morpion[ligne_index][0] == morpion[ligne_index][1] and morpion[ligne_index][0] == morpion[ligne_index][2] and estRemplie(morpion[ligne_index][0]):
                jeu_en_cours = False

        # On vérifie les colonnes.
        for ligne_index in range(3):
            if morpion[0][ligne_index] == morpion[1][ligne_index] and morpion[0][ligne_index] == morpion[2][ligne_index] and estRemplie(morpion[0][ligne_index]):
                jeu_en_cours = False

        # On vérifie l'égalité.
        # Pour faire cela, on itère tout les éléments
        # et si un élément n'est pas rempli, on est sûr de ne
        # pas avoir d'égalité.
        if (jeu_en_cours):
            égalité = True
            for ligne_index in range(3):
                for case_index in range(3):
                    if (not estRemplie(morpion[ligne_index][case_index])):
                        égalité = False

            if (égalité):
                jeu_en_cours = False

        input("Appuyez sur une touche pour continuer...")

    # On affiche la nouvelle grille avant d'afficher le résultat.
    effacer_ecran()
    afficher_tour(nb_tour)
    afficher_morpion(morpion)

    if (not égalité):
        # On remplie le score.
        score.vainqueur = joueur_actuel
        score.perdant   = adversaire_actuel
        score.points    = 50
        # On ajoute le score dans le fichier binaire.
        écrireScore(score)

        # On affiche la fin de jeu.
        print(séparateur_avec_titre("FIN") + "\n")
        print(centrer_couleur(couleur_joueur(joueur_actuel, joueur1, joueur2) + " a gagné en " + str(nb_tour) + " tours et remporte " + str(score.points) + " points !"))
        print(centrer_couleur(couleur_joueur(adversaire_actuel, joueur1, joueur2) + " a perdu."))
    else:
        # On affiche la fin de jeu.
        print(séparateur_avec_titre("ÉGALITÉ") + "\n")
        print(centrer_couleur("Aucun point n'est attribué."))

    # Permet d'éviter de revenir directement au lanceur.
    input("\nAppuyez sur Entrée pour continuer...")
