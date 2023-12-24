--1
CREATE PROCEDURE AfficherPilotesParVille
    @Ville VARCHAR(25)
AS
BEGIN
    SELECT *
    FROM pilote
    WHERE ville = @Ville;
END;

--2
CREATE PROCEDURE AfficherVolsParPilote
AS
BEGIN
    SELECT p.nom, v.*
    FROM pilote p
    JOIN vol v ON p.pil# = v.pilote;
END;