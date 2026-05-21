import sqlite3
import recherche
import date_de_retour


def import_sql():
    conn = sqlite3.connect('bibliotheque_agile.db')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS livres''')
    c.execute('''DROP TABLE IF EXISTS usagers''')
    c.execute('''CREATE TABLE livres (`idLivre` int(11) NOT NULL,`titre` varchar(255) NOT NULL,`auteur` varchar(255) DEFAULT NULL,`statut` varchar(255) DEFAULT 'DISPONIBLE',`rayon` varchar(255) DEFAULT NULL,`etagere` int(11) DEFAULT NULL);''')
    c.execute('''INSERT INTO `livres` (`idLivre`, `titre`, `auteur`, `statut`, `rayon`, `etagere`) VALUES
(1, 'Don Quichotte', 'Miguel De Cervantes', 'DISPONIBLE', 'A', 1),
(2, 'Les misérables', 'Victor Hugo', 'DISPONIBLE', 'B', 2),
(3, 'Hunger Games', 'Suzanne Collins', 'DISPONIBLE', 'C', 3),
(4, 'Harry Potter à l ecole des sorciers', 'J.K Rowling', 'DISPONIBLE', 'D', 1),
(5, 'Le Hobbit', 'J.R.R Tolkien', 'DISPONIBLE', 'A', 2),
(6, 'Lorenzaccio', 'Alfred de Musset', 'DISPONIBLE', 'B', 4),
(7, 'Les liasons dangereuses', 'Pierre Choderlos de Laclos', 'DISPONIBLE', 'C', 1),
(8, 'Le temps de l innocence', 'Edith Wharton', 'DISPONIBLE', 'D', 2),
(9, 'La crise de la culture', 'Annah Arendt', 'DISPONIBLE', 'A', 3),
(10, 'Pinocchio', 'Carlo Collodi', 'DISPONIBLE', 'B', 3),
(11, 'Dora et Diego', 'Leslie Valdes', 'DISPONIBLE', 'A', 2);''')
    
    c.execute('''CREATE TABLE usagers (
  idUsager int(11) NOT NULL,
  nom varchar(255) NOT NULL,
  prenom varchar(255) NOT NULL,
  contact varchar(255) NOT NULL
);''')
    conn.commit()
    conn.close()



if __name__ == "__main__":
    #import_sql()
    recherche.recherche_titre_auteur(titre="Don Quichotte")
    date_de_retour.calculer_date_de_retour("Don Quichotte", "Miguel De Cervantes")