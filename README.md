# Scrappe

Le but de l'exercice est de scrapper les donnees sur la page de jumia et ensuite connecté une base de données de notre choix pour recuper ses données.
Pour ce fait, nous devons creer une base de donnees avec :
CREATE DATABASE dbScrappe
ensuite on cree les tables avec:

CREATE TABLE Categorie 
(
  id INT PRIMARY KEY NOT NULL IDENTITY,//identify pour incrementer automatique les valeurs
  categorieNom VARCHAR(250),
  
);

use dbScrapper

CREATE TABLE Produit
(
  id INT PRIMARY KEY NOT NULL IDENTITY,
  produitNom VARCHAR(250),
  produitMarque varchar(250),
  produitcommentaire varchar(300),
  categorieNom varchar(250),
FOREIGN KEY (id) references Categorie
  
);
