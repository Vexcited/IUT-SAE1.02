from utils.effacer_ecran import effacer_ecran
from utils.titre import faire_titre

def définir_nom_joueur(index: int, étaitMêmeNom: bool = False) -> str:
    """
    Fonction permettant de choisir un nom pour l'utilisateur {index}
    pour un jeu donné.

    ## Entrée :
    
    - `index` ne peut être que `1` ou `2` (Joueur 1 ou Joueur 2)
    - `étaitMêmeNom` est définie dans le lanceur lorsque le joueur 2 entre le même nom d'utilisateur que le joueur 1.
      Permet l'affichage d'un message supplémentaire.
    """

    nom_utilisateur: str
    faire_robot: bool

    nom_utilisateur = ""
    faire_robot = False

    # Tant que l'utilisateur n'a pas entré de nom d'utilisateur,
    # on redemande un nom d'utilisateur.
    while nom_utilisateur == "":
        effacer_ecran()
        faire_titre("Joueur : " + str(index))

        faire_robot = input("Ce joueur est un robot ? (O/N) : ").upper() == "O"

        if (faire_robot):
            if index == 1:
                nom_utilisateur = "robot"
            else:
                nom_utilisateur = "robot2"
        else:
            if (étaitMêmeNom):
                print("Pensez à ne pas utiliser le même nom d'utilisateur que le joueur 1 !")

            nom_utilisateur = input("-> Joueur " + str(index) + " : ")
    
    return nom_utilisateur
