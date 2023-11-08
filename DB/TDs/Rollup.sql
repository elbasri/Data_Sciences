
CREATE TABLE Ventes (
    Produit VARCHAR(255),
    Ville VARCHAR(255),
    nbventes INT
);

-- Insertion des données dans la table Ventes
INSERT INTO Ventes (Produit, Ville, nbventes)
VALUES
    ('Ecran', 'Casa', 15),
    ('Ecran', 'Rabat', 10),
    ('Ecran', 'Fes', 10),
    ('Clavier', 'Casa', 15),
    ('Clavier', 'Rabat', 30),
    ('Clavier', 'Fes', 30),
    ('Souris', 'Casa', 10),
    ('Souris', 'Rabat', 10),
    ('Souris', 'Fes', 25);


-- Requests


--# SELECT produit, null, SUM(nbventes) as TotalVentes FROM Ventes group by Produit UNION SELECT null, Ville, SUM(nbventes) as TotalVentes FROM Ventes group by Ville
--#select Produit, Ville, SUM(nbventes) as TotalVentes FROM Ventes GROUP BY Produit, Ville WITH ROLLUP
--#SELECT Produit, Ville, SUM(nbventes) as TotalVentes FROM Ventes GROUP BY Produit, Ville  UNION  SELECT Produit, NULL, SUM(nbventes) as TotalVentes FROM Ventes GROUP BY Produit  UNION  SELECT NULL, Ville, SUM(nbventes) as TotalVentes FROM Ventes GROUP BY Ville  UNION  SELECT NULL, NULL, SUM(nbventes) as TotalVentes FROM Ventes;
--#select Produit, Ville, SUM(nbventes) as TotaleVentes from Ventes GROUP BY Produit, Ville WITH ROLLUP

--#CUBE is not suported by MYSQL:
--#SELECT Produit, Ville, SUM(nbventes) as TotalVentes FROM Ventes GROUP BY CUBE (Produit, Ville);

