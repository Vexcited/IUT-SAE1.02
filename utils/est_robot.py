def est_robot(joueur: str) -> bool:
    """
    fonction qui permet de tester si le joueur passé en argument est un robot
        entrée : le nom du joueur
        sortie : le résultat du test
    """
    return joueur == "robot" or joueur == "robot2"

def format_si_nom_robot(joueur: str) -> str:
    """
    Fonction qui permet de formater le nom du joueur si c'est un robot.
        entrée : le nom du joueur
        sortie : le nom formaté
    """
    if (not est_robot(joueur)):
        return joueur
    else:
        if (joueur == "robot"):
            return "Robot 1"
        else:
            return "Robot 2"