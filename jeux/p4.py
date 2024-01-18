from utils.afficher_tour import afficher_tour
from utils.titre import centrer_couleur, séparateur_avec_titre
from utils.input import demanderEntier
from utils.effacer_ecran import effacer_ecran
from utils.couleurs import réinitialisation_couleur, jaune, rouge_clair, couleur_joueur, gris_foncé_re
from scores.entrée import EntréeScore
from scores.fichier import écrireScore
from utils.est_robot import format_si_nom_robot
from random import choice

def calcul_points(nombre_tour : int) -> int:
    """
    Calcule les points en fonction du nombre de tours.
    """

    points : int
    points = 1000 // (nombre_tour * 2)
    
    return points

def afficher_p4(jeu: list[list[str]], colonne_restantes: list[int]) -> None:
    """
    Procédure qui permet d'afficher le jeu.
    
    ## Entrée :

    - `jeu`, un tableau de tableau de chaîne : grille du puissance 4.
    - `colonne_restantes`, une liste d'entiers : colonnes restantes.
    """

    index_ligne         : int
    index_case          : int
    ligne               : str
    ligne_col_restantes : str
    index_col           : int

    print("") # Saut de ligne avant la grille.

    print(centrer_couleur("╭╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╮"))
    for index_ligne in range(6):
        ligne = " │ "

        for index_case in range(7):
            ligne += jeu[index_ligne][index_case] + " "

        ligne += "│ "

        print(centrer_couleur(ligne))
    print(centrer_couleur("└───────────────┘"))

    ligne_col_restantes = "  "
    for index_col in range(1, 8):
        if index_col in colonne_restantes:
            ligne_col_restantes += str(index_col) + " "
        else:
            ligne_col_restantes += gris_foncé_re(str(index_col)) + " "

    ligne_col_restantes += " "

    print(centrer_couleur(ligne_col_restantes))
    print("") # Saut de ligne après la grille.

def dérouler_tour(joueur_actuel: str, joueur1: str, jeu: list[list[str]], colonne_restantes: list[int]) -> int:
    """
    Fonction qui déroule le tour de Puissance 4.

    ## Sortie :
    - `0` si on continue le jeu.
    - `1` si le `joueur_actuel` a gagné.
    - `2` si le jeu est terminé (égalité).
    """
    index_ligne : int
    index_case : int
    choix : int
    couleur : str

    # S'il n'y a plus de colonne restante, c'est une égalité. 
    if len(colonne_restantes) == 0:
        return 2

    # On récupère seulement la couleur.
    if joueur1 == joueur_actuel:
        couleur = jaune("") 
    # L'autre est forcément le joueur 2.
    else:
        couleur = rouge_clair("")

    # Si c'est un robot qui joue, un algorithme est donc lancé pour effectuer le tour du robot
    # sinon je joueur joue
    if joueur_actuel == "robot":
        choix = choice(colonne_restantes)

        print(réinitialisation_couleur(couleur + joueur_actuel), "a choisi la colonne", choix, "!")
    else:
        # On demande au joueur de choisir une colonne.
        choix = demanderEntier(réinitialisation_couleur(couleur + joueur_actuel) + ", choisissez une colonne : ")

        while choix not in colonne_restantes :
            choix = demanderEntier(réinitialisation_couleur(couleur + joueur_actuel) + ", choisissez une colonne encore disponible : ")

    # Test pour savoir a quel endroit de la colonne choisie le pion dois se mettre
    if jeu[5][choix-1] == '.':
        jeu[5][choix-1] = réinitialisation_couleur(couleur + "O")
    else:
        index_ligne = 0

        while (index_ligne >= 0 and jeu[5 - index_ligne][choix - 1] != "."):
            index_ligne += 1

        jeu[5 - index_ligne][choix - 1] = réinitialisation_couleur(couleur + "O")

    # Si la colonne est pleine, on l'enlève des colonnes restantes.
    if jeu[0][choix - 1] != ".":
        colonne_restantes.remove(choix)

    # Test ligne gagnante.
    for index_ligne in range(3):
        for index_case in range(6):
            if jeu[index_ligne][index_case] == jeu[index_ligne+1][index_case] and jeu[index_ligne+2][index_case] == jeu[index_ligne+3][index_case] and jeu[index_ligne][index_case] == jeu[index_ligne+3][index_case] and jeu[index_ligne][index_case] != ".":
                return 1

    # Test colonne gagnante.
    for index_ligne in range(6):
        for index_case in range(3):
            if jeu[index_ligne][index_case] == jeu[index_ligne][index_case+1] and jeu[index_ligne][index_case+2] == jeu[index_ligne][index_case+3] and jeu[index_ligne][index_case] == jeu[index_ligne][index_case+3] and jeu[index_ligne][index_case] != ".":
                return 1

    # Test diagonale : haut de droite -> bas à gauche.
    for index_ligne in range(3):
        for index_case in range(4):
            if jeu[index_ligne][index_case] == jeu[index_ligne+1][index_case+1] and jeu[index_ligne+2][index_case+2] == jeu[index_ligne+3][index_case+3] and jeu[index_ligne][index_case] == jeu[index_ligne+3][index_case+3] and jeu[index_ligne][index_case] != ".":
                return 1

    # Test diagonale : haut à gauche -> bas à droite.
    for index_ligne in range(3):
        for index_case in range(4):
            if jeu[index_ligne+3][index_case] == jeu[index_ligne+2][index_case+1] and jeu[index_ligne+1][index_case+2] == jeu[index_ligne][index_case+3] and jeu[index_ligne+3][index_case] == jeu[index_ligne][index_case+3] and jeu[index_ligne+3][index_case] != ".":
                return 1
    
    input("Appuyez sur une touche pour continuer...")
    # Personne a gagné, on continue la partie.
    return 0

def main_p4(joueur1: str, joueur2: str) -> None:
    """
    Procédure qui sert de point d'entrée pour le lanceur.
    C'est la procédure principale du jeu Puissance 4.

    * Le joueur 1 jouera avec "O".
    * Le joueur 2 jouera avec "X".

    ## Entrée :

    - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
    - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
    """
    
    colonne_restantes : list[int]
    jeu               : list[list[str]]
    nb_tour           : int
    tour_résultat     : int
    score             : EntréeScore
    joueur_actuel     : str
    adversaire_actuel : str

    colonne_restantes = list(range(1, 8))
    jeu = [[".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "."]]
    
    nb_tour       = 1
    tour_résultat = 0 # Par défaut, on veut continuer le jeu.

    score = EntréeScore()
    score.type_jeu = "puissance_4"

    # Au début du jeu, on est au tour 1.
    joueur_actuel     = joueur1
    adversaire_actuel = joueur2

    while tour_résultat == 0:
        effacer_ecran()
        afficher_tour(nb_tour)
        afficher_p4(jeu, colonne_restantes)

        if nb_tour % 2 == 1:
            joueur_actuel     = joueur1
            adversaire_actuel = joueur2
        else:
            joueur_actuel     = joueur2
            adversaire_actuel = joueur1

        tour_résultat = dérouler_tour(joueur_actuel, joueur1, jeu, colonne_restantes)
        nb_tour += 1

    effacer_ecran()
    afficher_tour(nb_tour)
    afficher_p4(jeu, colonne_restantes)

    # Partie normale avec un vainqueur.
    if tour_résultat == 1:
        # On remplie le score.
        score.vainqueur = joueur_actuel
        score.perdant   = adversaire_actuel
        score.points    = calcul_points(nb_tour)
        # On ajoute le score dans le fichier binaire.
        écrireScore(score)

        # On affiche la fin de jeu.
        print(séparateur_avec_titre("FIN") + "\n")
        print(centrer_couleur(couleur_joueur(format_si_nom_robot(joueur_actuel), joueur1, joueur2) + " a gagné en " + str(nb_tour) + " tours et remporte " + str(score.points) + " points !"))
    # S'il y a égalité...
    elif tour_résultat == 2:
        # On affiche la fin de jeu.
        print(séparateur_avec_titre("ÉGALITÉ") + "\n")
        print(centrer_couleur("Aucun point n'est attribué."))

    # Permet d'éviter de revenir directement au lanceur.
    input("\nAppuyez sur Entrée pour continuer...")
