-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 06 mai 2026 à 16:32
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `bibliothèque_agile`
--

-- --------------------------------------------------------

--
-- Structure de la table `livres`
--

CREATE TABLE `livres` (
  `idLivre` int(11) NOT NULL,
  `titre` varchar(255) NOT NULL,
  `auteur` varchar(255) DEFAULT NULL,
  `statut` enum('DISPONIBLE','RESERVE','EMPRUNTE') DEFAULT 'DISPONIBLE',
  `rayon` varchar(255) DEFAULT NULL,
  `etagere` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `livres`
--

INSERT INTO `livres` (`idLivre`, `titre`, `auteur`, `statut`, `rayon`, `etagere`) VALUES
(1, 'Don Quichotte', 'Miguel De Cervantes', 'DISPONIBLE', 'A', 1),
(2, 'Les misérables', 'Victor Hugo', 'DISPONIBLE', 'B', 2),
(3, 'Hunger Games', 'Suzanne Collins', 'DISPONIBLE', 'C', 3),
(4, 'Harry Potter à l\'école des sorciers', 'J.K Rowling', 'DISPONIBLE', 'D', 1),
(5, 'Le Hobbit', 'J.R.R Tolkien', 'DISPONIBLE', 'A', 2),
(6, 'Lorenzaccio', 'Alfred de Musset', 'DISPONIBLE', 'B', 4),
(7, 'Les liasons dangereuses', 'Pierre Choderlos de Laclos', 'DISPONIBLE', 'C', 1),
(8, 'Le temps de l\'innocence', 'Edith Wharton', 'DISPONIBLE', 'D', 2),
(9, 'La crise de la culture', 'Annah Arendt', 'DISPONIBLE', 'A', 3),
(10, 'Pinocchio', 'Carlo Collodi', 'DISPONIBLE', 'B', 3),
(11, 'Dora et Diego', 'Leslie Valdes', 'DISPONIBLE', 'A', 2);

-- --------------------------------------------------------

--
-- Structure de la table `usagers`
--

CREATE TABLE `usagers` (
  `idUsager` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `livres`
--
ALTER TABLE `livres`
  ADD PRIMARY KEY (`idLivre`);

--
-- Index pour la table `usagers`
--
ALTER TABLE `usagers`
  ADD PRIMARY KEY (`idUsager`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `livres`
--
ALTER TABLE `livres`
  MODIFY `idLivre` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT pour la table `usagers`
--
ALTER TABLE `usagers`
  MODIFY `idUsager` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
