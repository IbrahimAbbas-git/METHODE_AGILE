# coding: utf-8
import sqlite3


def recherche_titre_auteur(titre=None, auteur=None):
    conn= sqlite3.connect('bibliotheque_agile.db')
    c = conn.cursor()
    if titre is not None and auteur is None :
        print(f"Recherche du livre avec le titre '{titre}'")
        #rechercher dans la db avec SELECT * FROM livres WHERE titre = '{titre}'
        c.execute(f"SELECT * FROM livres WHERE titre = '{titre}'")
        resultats = c.fetchall()
        print(resultats)

    if auteur is not None and titre is None :
        print(f"Recherche du livre avec l'auteur '{auteur}'")
        #rechercher dans la db avec SELECT * FROM livres WHERE auteur = '{auteur}'
        c.execute(f"SELECT * FROM livres WHERE auteur = '{auteur}'")
        resultats = c.fetchall()
        print(resultats)
    if titre is not None and auteur is not None :
        print(f"Recherche du livre avec le titre '{titre}' et l'auteur '{auteur}'")
        #rechercher dans la db avec SELECT * FROM livres WHERE titre = '{titre}' AND auteur = '{auteur}'
        c.execute(f"SELECT * FROM livres WHERE titre = '{titre}' AND auteur = '{auteur}'")
        resultats = c.fetchall()
        print(resultats)
    conn.close()
    liste_potentielle = None
    return liste_potentielle
