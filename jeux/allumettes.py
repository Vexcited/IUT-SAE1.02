from utils.afficher_tour import afficher_tour
from utils.effacer_ecran import effacer_ecran
from utils.titre import séparateur_avec_titre
from utils.input import demanderEntier
from utils.centrer import centrer
from scores.entrée import EntréeScore
from scores.fichier import écrireScore
from random import randint

def afficher_allumettes(nb_allumettes : int) -> None:
    """
    Procédure qui permet d'afficher le nombre d'allumettes restantes en jeu.
    On ajoute un saut de ligne avant et après les allumettes pour espacer
    le jeu des autres éléments affichés à l'écran.

    ## Entrée :
    
    - `nb_allumettes`, un entier, qui représente le nombre d'allumettes que l'on va afficher.
    """

    print("") # Saut de ligne
    print(centrer("O " * nb_allumettes))
    print(centrer("│ " * nb_allumettes))
    print(centrer("│ " * nb_allumettes))
    print(centrer("│ " * nb_allumettes))
    print("") # Saut de ligne


def dérouler_tour(joueur: str, nb_tour: int, nb_allumettes: int) -> int:
    """
    Fonction qui déroule le tour d'un joueur.
    1. On affiche le tour
    2. On affiche les allumettes
    3. On demande au joueur combien d'allumettes iel veut retirer
    4. On traite la réponse donnée
    
    ## Entrée :
    
    - joueur, une chaîne, qui représente le nom du joueur qui est entrain de jouer.
    - nb_tour, un entier, qui représente le nombre de tours actuel.
                On commence la partie au "Tour 1", donc `nb_tour` sera 1.
    - nb_allumettes, un entier: le nombre d'allumettes encore en jeu
    
    ## Sortie :

    Un entier qui représente le nombre d'allumettes encore en jeu à la fin du tour.
    Retourne `-1` dans le cas où la partie est terminée.
    """
    choix_allumettes : int
    
    # On efface l'écran pour avoir un affichage
    # plus propre des allumettes.
    effacer_ecran()
    afficher_tour(nb_tour)
    afficher_allumettes(nb_allumettes)

    print("Il reste ", nb_allumettes, "allumettes...")

    # Si c'est un robot qui joue, un algorithme est donc lancé pour effectuer le tour du robot
    # sinon le joueur joue
    if joueur == "robot":
        if nb_allumettes > 8 :
            choix_allumettes = randint(1, 3)
        elif nb_allumettes > 5 :
            choix_allumettes = nb_allumettes - 5
        elif nb_allumettes > 4 :
            choix_allumettes = randint(1, 3)
        elif nb_allumettes > 1 :
            choix_allumettes = nb_allumettes - 1
        else:
            choix_allumettes = 1
        
        print(joueur, "prends", choix_allumettes, "allumettes !")
    else:
        choix_allumettes = demanderEntier(joueur + " : Combien d'allumettes prenez-vous ? (1, 2 ou 3) : ")

    # Lorsque l'on prend les allumettes qui restent,
    # on perd la partie.
    if choix_allumettes >= nb_allumettes:
        # On renvoie le signal de fin de jeu.
        return -1

    # On vérifie que le joueur a bien entré un nombre d'allumettes valide.
    while choix_allumettes not in [1, 2, 3]:
        choix_allumettes = demanderEntier(joueur + " : Le nombre d'allumettes à retirer du jeu doit être 1, 2 ou 3 ! : ")
        
    input("Appuyez sur une touche pour continuer...")
    
    # On retourne le nombre d'allumettes restantes.
    return nb_allumettes - choix_allumettes

def main_allumettes(joueur1: str, joueur2: str) -> None:
    """
    Procédure qui sert de point d'entrée pour le lanceur.
    C'est la procédure principale du jeu d'allumettes.

    Le jeu commence au tour 1 avec 20 allumettes.
    C'est `joueur1` qui commence la partie.

    ## Entrée :

    - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
    - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
    """

    nb_tour           : int
    nb_allumettes     : int
    joueur_actuel     : str
    adversaire_actuel : str
    score             : EntréeScore

    # On commence réellement au tour 1.
    # Voir la boucle `while` en dessous.
    nb_tour = 0
    # Le nombre d'allumettes avec lequel on commence.
    nb_allumettes = 20
    score = EntréeScore()
    score.type_jeu = "allumettes"

    # Au début du jeu, on est au tour 1.
    joueur_actuel     = joueur1
    adversaire_actuel = joueur2

    while nb_allumettes != -1:
        nb_tour += 1
        
        # On récupère le nom du joueur qui doit jouer.
        if nb_tour % 2 == 1:
            joueur_actuel     = joueur1
            adversaire_actuel = joueur2
        else:
            joueur_actuel     = joueur2
            adversaire_actuel = joueur1
        
        # On lui demande de jouer.
        nb_allumettes = dérouler_tour(joueur_actuel, nb_tour, nb_allumettes)

    # On remplie le score.
    score.vainqueur = adversaire_actuel
    score.perdant   = joueur_actuel
    score.points    = 50
    # On ajoute le score dans le fichier binaire.
    écrireScore(score)

    # On affiche la fin de jeu.
    print("\n" + séparateur_avec_titre("FIN") + "\n")
    print(centrer(adversaire_actuel + " a gagné en " + str(nb_tour) + " tours et remporte " + str(score.points) + " points !"))
    print(centrer(joueur_actuel + " a perdu."))

    # Permet d'éviter de revenir directement au lanceur.
    input("\nAppuyez sur Entrée pour continuer...")
