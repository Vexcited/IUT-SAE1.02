from typing import Union
from scores.entrée import EntréeScore, EntréePointsUtilisateur
from utils.est_robot import est_robot

def pointsParUtilisateur(scores: list[EntréeScore]) -> list[EntréePointsUtilisateur]:
    """
    Fonction qui transforme une liste d'entrées de score en une liste d'entrées de points par utilisateur.
    Elle permet de calculer les points cumulés par utilisateur.

    Entrée : `scores` est une liste d'entrées de score.
    Sortie : Une liste d'entrées de points par utilisateur.      
    """

    scores_utilisateurs: list[EntréePointsUtilisateur]
    scores_utilisateurs_index: int
    entrée_utilisateur: Union[EntréePointsUtilisateur, None]
    entrée: EntréeScore

    scores_utilisateurs = []

    for entrée in scores:
        # On vérifie qu'on ne traite pas les scores des robots
        if not est_robot(entrée.vainqueur):
            entrée_utilisateur = None

            # On cherche si l'utilisateur a déjà joué.
            scores_utilisateurs_index = 0
            # On fait attention à ne pas dépasser la taille de la liste.
            while entrée_utilisateur is None and scores_utilisateurs_index < len(scores_utilisateurs):
                if scores_utilisateurs[scores_utilisateurs_index].nom_utilisateur == entrée.vainqueur:
                    # On a trouvé une entrée et on la réutilise.
                    entrée_utilisateur = scores_utilisateurs[scores_utilisateurs_index]
                else:
                    scores_utilisateurs_index += 1

            # Si l'utilisateur n'a pas encore joué, on crée une entrée pour lui.
            if entrée_utilisateur is None:
                entrée_utilisateur = EntréePointsUtilisateur()
                entrée_utilisateur.nom_utilisateur = entrée.vainqueur
                entrée_utilisateur.points = 0
                entrée_utilisateur.nombre_parties = 0
                scores_utilisateurs.append(entrée_utilisateur)

            # On met à jour les points de l'utilisateur.
            entrée_utilisateur.points += entrée.points
            entrée_utilisateur.nombre_parties += 1

    return scores_utilisateurs

def trierPoints(scores: list[EntréePointsUtilisateur]) -> list[EntréePointsUtilisateur]:
    """
    Fonction qui trie une liste d'entrées de points par utilisateur
    par ordre décroissant de points cumulés.

    Entrée : `scores` est une liste d'entrées de points par utilisateur.
    Sortie : Une liste d'entrées de points par utilisateur triée par ordre décroissant de points cumulés.
    """

    scores_triés: list[EntréePointsUtilisateur]
    entrée: EntréePointsUtilisateur
    index: int

    scores_triés = []

    for entrée in scores:
        index = 0

        # On cherche la place de l'entrée dans la liste triée.
        while index < len(scores_triés) and entrée.points < scores_triés[index].points:
            index += 1

        # On insère l'entrée à la bonne place.
        scores_triés.insert(index, entrée)

    return scores_triés