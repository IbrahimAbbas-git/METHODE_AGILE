import sqlite3
from datetime import timedelta

def calculer_date_de_retour(livre, auteur):
    conn= sqlite3.connect('bibliotheque_agile.db')
    c = conn.cursor()
    c.execute(f"SELECT idlivre FROM livres WHERE titre = '{livre}' AND auteur = '{auteur}'")
    resultat = c.fetchone()
    if resultat is not None:
        idLivre = resultat[0]
        c.execute(f"SELECT date FROM emprunte WHERE idLivre = {idLivre}")
        resultat_date = c.fetchone()
        if resultat_date is not None:
            date_emprunt = resultat_date[0]
            #calculer la date de retour en ajoutant 21 jours à la date d'emprunt
            date_retour = date_emprunt + timedelta(days=21)
            print(f"La date de retour pour le livre '{livre}' de l'auteur '{auteur}' est le {date_retour}")
        else:
            print(f"Le livre '{livre}' de l'auteur '{auteur}' n'est pas emprunté actuellement.")
    else : 
        print(f"Le livre '{livre}' de l'auteur '{auteur}' n'existe pas dans la bibliothèque.")
    conn.close()

    def liste_livres_en_retard():
        conn= sqlite3.connect('bibliotheque_agile.db')
        c = conn.cursor()
        c.execute("SELECT idLivre FROM emprunte")
        resultats = c.fetchall()
        for idLivre in resultats:
            c.execute(f"SELECT date FROM emprunte WHERE idLivre = {idLivre[0]}")
            resultat_date = c.fetchone()
            if resultat_date is not None:
                date_emprunt = resultat_date[0]
                #calculer la date de retour en ajoutant 21 jours à la date d'emprunt
                date_retour = date_emprunt + timedelta(days=21)
                print(f"Le livre avec l'ID {idLivre[0]} est en retard et doit être retourné le {date_retour}")
        conn.close()