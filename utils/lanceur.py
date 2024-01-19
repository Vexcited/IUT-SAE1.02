from joueurs.selection import définir_nom_joueur
from scores.fichier import scoresPourJeu
from scores.entrée import EntréeScore, EntréePointsUtilisateur
from scores.points import pointsParUtilisateur, trierPoints
from utils.effacer_ecran import effacer_ecran
from utils.titre import faire_titre, centrer_avec_bordures, séparateur_avec_bordures_vers_haut, centrer_couleur_avec_bordures
from utils.est_robot import est_robot
from utils.est_robot import difficulté_robot

from jeux.devinette import main_devinette
from jeux.allumettes import main_allumettes
from jeux.morpion import main_morpion
from jeux.p4 import main_p4

def préJeu(type_jeu: str) -> None:
    """
    Procédure qui affiche un menu intermédiaire
    avant de lancer un jeu qui affiche les scores précédents sur ce jeu.
    
    On peut ici choisir de démarrer le jeu en tapant `1` ou de revenir
    au menu principal en tapant `0`.

    Permet en même temps de demander si 

    Entrée : `type_jeu` peut être `"devinette"`, `"allumettes"`, `"morpion"` ou `"puissance_4"`.
    """

    premier_lancement: bool
    rejouer: bool
    sélection: str
    difficulté_robot1: str
    difficulté_robot2: str
    nom_joueur_1: str
    nom_joueur_2: str
    scores: list[EntréeScore]
    entrée: EntréePointsUtilisateur
    entrée_index: int
    nom_utilisateur: str
    scores_par_utilisateur: list[EntréePointsUtilisateur]

    premier_lancement = True
    rejouer = True # On initialise la variable rejouer à True pour que le jeu se lance au moins une fois.

    while rejouer:
        effacer_ecran()
        scores = scoresPourJeu(type_jeu)
        scores_par_utilisateur = trierPoints(pointsParUtilisateur(scores))

        # On affiche les scores.
        faire_titre("Tableau des scores pour le jeu : " + type_jeu.replace("_", " ").upper(), bas_arrondis=False)
        if (len(scores_par_utilisateur) == 0):
            print(
                centrer_avec_bordures(""),
                centrer_avec_bordures("(Aucun score enregistré, pour le moment...)"),
                centrer_avec_bordures(""),
                sep="\n"
            )
        else:
            for entrée_index in range(len(scores_par_utilisateur)):
                entrée = scores_par_utilisateur[entrée_index]
                nom_utilisateur = entrée.nom_utilisateur + "\033[0m"

                # On ajoute des couleurs sur les trois premiers.
                if entrée_index == 0:
                    nom_utilisateur = "\033[1;33m" + nom_utilisateur
                elif entrée_index == 1:
                    nom_utilisateur = "\033[0;37m" + nom_utilisateur
                elif entrée_index == 2:
                    nom_utilisateur = "\033[0;33m" + nom_utilisateur

                print(centrer_couleur_avec_bordures(nom_utilisateur + "    " + str(entrée.points) + " | " + str(entrée.nombre_parties) + " partie(s) jouée(s)"))
        
        print(séparateur_avec_bordures_vers_haut())
        
        sélection = ""
        # On vérifie que l'utilisateur a entré une sélection valide.
        while sélection != "1" and sélection != "0":
            # On demande à l'utilisateur s'il veut jouer.
            if premier_lancement:
                print("\nVoulez-vous jouer ?\n")
            else:
                print("\nVoulez-vous rejouer ?\n")

            print("\t1 │ Oui")
            print("\t0 │ Non, revenir au menu principal")
            sélection = input("\n-> Sélection(1,0) : ").strip()
            
            if sélection != "1" and sélection != "0":
                print("Sélection invalide !")

        difficulté_robot1 = ""
        difficulté_robot2 = ""
        # Si l'utilisateur veut jouer, on lance le jeu.
        if sélection == "1":
            # On demande le nom d'utilisateur de chaque joueur.
            nom_joueur_1 = définir_nom_joueur(1)

            if est_robot(nom_joueur_1):
                difficulté_robot1 = difficulté_robot()

            nom_joueur_2 = définir_nom_joueur(2)

            if est_robot(nom_joueur_2):
                difficulté_robot2 = difficulté_robot()
            
            # Le joueur 2 ne doit pas avoir le même nom que le joueur 1.
            while (nom_joueur_2 == nom_joueur_1):
                nom_joueur_2 = définir_nom_joueur(2, True)

            # On lance le jeu.
            effacer_ecran()
            if type_jeu == "devinette":
                main_devinette(nom_joueur_1, nom_joueur_2, difficulté_robot1, difficulté_robot2)
            elif type_jeu == "allumettes":
                main_allumettes(nom_joueur_1, nom_joueur_2, difficulté_robot1, difficulté_robot2)
            elif type_jeu == "morpion":
                main_morpion(nom_joueur_1, nom_joueur_2, difficulté_robot1, difficulté_robot2)
            elif type_jeu == "puissance_4":
                main_p4(nom_joueur_1, nom_joueur_2, difficulté_robot1, difficulté_robot2)

            # Une fois que le jeu a été joué,
            # on dit qu'il a déjà été lancé au moins une fois.
            if premier_lancement:
                premier_lancement = False
        else:
            # Si l'utilisateur ne veut pas jouer, on arrête la boucle.
            rejouer = False


