import math
import random

def recherche_titre_auteur(titre=None, auteur=None):
    if titre is not None and auteur is None :
        print(f"Recherche du livre avec le titre '{titre}'")
        #rechercher dans la db avec SELECT * FROM livres WHERE titre = '{titre}'
    if auteur is not None and titre is None :
        print(f"Recherche du livre avec l'auteur '{auteur}'")
        #rechercher dans la db avec SELECT * FROM livres WHERE auteur = '{auteur}'
    if titre is not None and auteur is not None :
        print(f"Recherche du livre avec le titre '{titre}' et l'auteur '{auteur}'")
        #rechercher dans la db avec SELECT * FROM livres WHERE titre = '{titre}' AND auteur = '{auteur}'
    liste_potentielle = None
    return liste_potentielle
