--TP 1:
--1 Lister les pilotes avec le code, le nom, le code postal et la ville du pilote
SELECT p.pil#, p.nom, p.CodePostal, p.ville FROM pilote p;

--2 Trier la liste précédente par code postal puis ville
SELECT p.pil#, p.nom, p.CodePostal, p.ville FROM pilote p ORDER BY p.CodePostal, p.ville;

--3 Trier la liste précédente par code postal puis ville en ordre décroissant
SELECT p.pil#, p.nom, p.CodePostal, p.ville FROM pilote p ORDER BY p.CodePostal DESC, p.ville DESC;

--4 Quels sont les types d’avion dont la capacité est inférieure à 300 passagers
SELECT av.typeavion FROM avion av WHERE av.Capacite < 300;

--5
SELECT av.typeavion FROM avion av WHERE av.Capacite < 300;

--6 Quels sont les vols au départ de Nice entre 12h et 14h ?
SELECT vol.vol FROM vol WHERE vol.villedepart = 'Nice' AND (vol.heuredepart >= '12:00:00' AND vol.heuredepart <= '14:00:00');

--7    Dans combien de villes différentes sont localisés des avions ?
SELECT COUNT(DISTINCT av.ville) FROM avion av;

--8    Donnez les avions de marque Airbus localisés dans une ville différente de Nice et dont la capacité est inférieure à 300 passagers.
SELECT av.avion FROM avion av WHERE av.Marque = 'Airbus' AND av.ville <> 'Nice' AND av.Capacite < 300;

--9 a 13
CREATE PROCEDURE GetAllQueries
AS
BEGIN
    -- Query 9
    SELECT v.villedepart, COUNT(*) AS NombreDeVols
    FROM vol v
    GROUP BY v.villedepart
    HAVING COUNT(*) > 1;

    -- Query 10
    SELECT a.ville, COUNT(*) AS NombreAvions, MIN(a.Capacite) AS CapaciteMin, MAX(a.Capacite) AS CapaciteMax
    FROM avion a
    GROUP BY a.ville;

    -- Query 11
    SELECT a.ville, COUNT(*) AS NombreAvions, MIN(a.Capacite) AS CapaciteMin, MAX(a.Capacite) AS CapaciteMax
    FROM avion a
    WHERE a.Capacite > 300
    GROUP BY a.ville;

    -- Query 12
    SELECT a.ville, AVG(a.Capacite) AS CapaciteMoyenne
    FROM avion a
    GROUP BY a.ville
    HAVING COUNT(*) > 1;

    -- Query 13
    SELECT p.nom
    FROM pilote p
    WHERE p.nom LIKE 'S%';
END
GO

EXEC GetAllQueries;