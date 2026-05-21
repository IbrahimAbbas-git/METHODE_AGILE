import sqlite3
from datetime import datetime, timedelta

def reserver_livre(livre, auteur, idUsager):
    conn= sqlite3.connect('bibliotheque_agile.db')
    c = conn.cursor()
    c.execute(f"SELECT idLivre FROM livres WHERE titre = '{livre}' AND auteur = '{auteur}'")
    resultat = c.fetchone()
    if resultat is not None:
        idLivre = resultat[0]
        c.execute(f"INSERT INTO emprunte (idLivre, idUsager, date) VALUES ({idLivre}, {idUsager}, {datetime.now().date()})")
        c.execute(f"UPDATE livres SET statut = 'EMPRUNTE' WHERE idLivre = {idLivre}")
        conn.commit()
        print(f"Le livre '{livre}' de l'auteur '{auteur}' a été réservé par l'usager avec l'ID {idUsager}.")
    else : 
        print(f"Le livre '{livre}' de l'auteur '{auteur}' n'existe pas dans la bibliothèque.")
    conn.close()

def rendu_livre(livre,auteur,idUsager):
    conn= sqlite3.connect('bibliotheque_agile.db')
    c = conn.cursor()
    c.execute(f"SELECT idLivre FROM livres WHERE titre = '{livre}' AND auteur = '{auteur}'")
    resultat = c.fetchone()
    if resultat is not None:
        idLivre = resultat[0]
        c.execute(f"SELECT date FROM emprunte WHERE idLivre = {idLivre}")
        date_emprunt = c.fetchone()
        c.execute(f"DELETE FROM emprunte WHERE idLivre = {idLivre} AND idUsager = {idUsager}")
        c.execute(f"UPDATE livres SET statut = 'DISPONIBLE' WHERE idLivre = {idLivre}")
        conn.commit()
        print(f"Le livre '{livre}' de l'auteur '{auteur}' a été rendu par l'usager avec l'ID {idUsager} emprunté le {date_emprunt[0]}.")
    else : 
        print(f"Le livre '{livre}' de l'auteur '{auteur}' n'existe pas dans la bibliothèque.")
    conn.close()