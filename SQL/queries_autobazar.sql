--15.11.2021 OPTIMALIZACE A TVORBA VIEWPOINTU

-- dulezity select vseho!!!!
select Vozidlo.AutoID, Znacka.Nazev, Model.NazevModelu, Vozidlo.Motor, Palivo.Nazev, ZemePuvodu.NazevZeme, Vozidlo.StavKilometru, Vozidlo.DatumVyroby, vozidlo.DatumVlozeni FROM Model
LEFT JOIN Znacka on Model.ZnackaID = Znacka.ZnackaID
JOIN Vozidlo on vozidlo.ModelID = model.ModelID
LEFT JOIN Palivo on Palivo.PalivoID = Vozidlo.PalivoID
LEFT JOIN ZemePuvodu on ZemePuvodu.ZemePuvoduID = Vozidlo.ZemePuvoduID;

select * from TabulkaVozidel;

 --1 vypis vsechny znacky ktere maji najeto do 200 tisic km
SELECT Znacka.Nazev, StavKilometru FROM Model
LEFT JOIN Znacka ON Znacka.ZnackaID = Model.ZnackaID 
LEFT JOIN Vozidlo ON Vozidlo.ModelID = Model.ModelID 
WHERE Model.ModelID in (SELECT AutoID FROM Vozidlo) AND StavKilometru < 200000;


--3 Vypíše poèet aut každé znaèky, která má naftu
SELECT Znacka.Nazev, COUNT(PalivoID) as pocet FROM Znacka 
RIGHT JOIN Model ON Model.ZnackaID = Znacka.ZnackaID
LEFT JOIN Vozidlo ON Vozidlo.ModelID = Model.ModelID 
WHERE PalivoID in (SELECT PalivoID FROM Palivo WHERE Nazev like 'Nafta') GROUP BY Znacka.Nazev;


--4 Vybere znaèky a model + motor aut ktera jsou rezervovaná na pøíští mìsíc
 SELECT DISTINCT TabulkaVozidel.Znacka, TabulkaVozidel.Model, TabulkaVozidel.Motorizace, tbl.pocetRezervaci FROM TabulkaVozidel
 JOIN (SELECT AutoID, COUNT(RezervaceProhlidkyID) as pocetRezervaci FROM RezervaceProhlidky GROUP BY AutoID) AS TBL ON tbl.AutoID = TabulkaVozidel.AutoID 
 LEFT JOIN RezervaceProhlidky ON RezervaceProhlidky.AutoID = TabulkaVozidel.AutoID
 WHERE DatumRezervace < GETDATE()+30;
  


-- JEDNA DVOUSLOUPECKOVA TABULKA : SELECT AutoID, COUNT(RezervaceProhlidkyID) as pocet FROM RezervaceProhlidky GROUP BY AutoID;

SELECT Znacka.Nazev, Vozidlo.AutoID FROM Znacka 
JOIN Model ON Znacka.ZnackaID = Model.ZnackaID 
JOIN Vozidlo ON Vozidlo.ModelID = Model.ModelID

--- DRUHA DVOUSLOUPECKOVA TABULKA: (SELECT AutoID, COUNT(RezervaceProhlidkyID) as pocetRezervaci FROM RezervaceProhlidky GROUP BY AutoID)



--5 Zobrazí všechna auta (model, znaèku, motor a zemì pùvodu), která pochazí z Èeska a mají vytvoøenou rezervaci 

SELECT Znacka.Nazev, Model.NazevModelu, Vozidlo.Motor, ZemePuvodu.NazevZeme FROM Znacka 
JOIN Model ON Znacka.ZnackaID = Model.ZnackaID
JOIN Vozidlo ON Vozidlo.ModelID= Model.ModelID
LEFT JOIN ZemePuvodu ON ZemePuvodu.ZemePuvoduID = Vozidlo.ZemePuvoduID
WHERE AutoID IN (SELECT DISTINCT AutoID FROM RezervaceProhlidky) AND ZemePuvodu.NazevZeme LIKE 'Èeská%';



--6 Vypište znaèky aut a jejich prùmìrnou cenu každé znaèky 
SELECT Tabulkavozidel.Znacka, AVG(TabulkaVozidel.Cena) as PrumernaCena FROM TabulkaVozidel GROUP BY Tabulkavozidel.Znacka;


--7 Vypište poèet zákazníkù, kteøí si rezervovali benzínová auta
SELECT TabulkaVozidel.Palivo, COUNT(Zakaznik.ZakaznikID) as pocetZakazniku FROM TabulkaVozidel
 JOIN RezervaceProhlidky ON RezervaceProhlidky.AutoID = TabulkaVozidel.AutoID
 LEFT JOIN Zakaznik ON Zakaznik.ZakaznikID = RezervaceProhlidky.ZakaznikID WHERE TabulkaVozidel.Palivo like 'Benzín' GROUP BY TabulkaVozidel.Palivo;

--8 Vypište nejstarší auto  na skladì 
SELECT Znacka, Model, Motorizace, DatumVyroby FROM TabulkaVozidel WHERE DatumVyroby <= (SELECT MIN(DatumVyroby) FROM TabulkaVozidel) ;

--9 Vypište 5 nejmladších nerezervovaných aut

SELECT TOP 5 Znacka, DatumVyroby FROM TabulkaVozidel 
WHERE TabulkaVozidel.AutoID NOT IN (SELECT AutoID FROM RezervaceProhlidky )
ORDER BY DatumVyroby DESC;


--10 Vypište poèet všech nerezervovaných aut (Znaèka, model, motorizace JE u aut VYPSANÁ ) + vypsat na potvrzení, že mají opravdu maji nulu :] 
SELECT TabulkaVozidel.Znacka , TabulkaVozidel.Model, TabulkaVozidel.Motorizace, COUNT (RezervaceProhlidkyID) as rezervace FROM TabulkaVozidel 
left JOIN RezervaceProhlidky ON TabulkaVozidel.AutoID = RezervaceProhlidky.AutoID 
WHERE RezervaceProhlidkyID is NULL OR RezervaceProhlidkyID = '' 
GROUP BY TabulkaVozidel.Znacka, TabulkaVozidel.Model, TabulkaVozidel.Motorizace HAVING Motorizace != '' and Motorizace is not null;

--11 Smazat auta, která nemají vyuplnìnou žádnou znaèku èi model
DELETE FROM Vozidlo WHERE ModelID IS NULL or ModelID  = ' ';

-- 12 Nastaví datum vložení aut, které nemají ID 1 a nastaví datum výroby u aut, které mají model vozida Octavia
UPDATE Vozidlo SET DatumVlozeni  = DATEADD(YEAR,-5, GETDATE() ) WHERE AutoID != 1;
UPDATE Vozidlo SET Vozidlo.DatumVyroby  = '2000-10-09' FROM Vozidlo
LEFT JOIN Model ON Model.ModelID = Vozidlo.ModelID WHERE Model.NazevModelu = 'Octavia';


--12 Smazat Rezervace jejichž ID je mezi 4 a 7
DELETE FROM RezervaceProhlidky WHERE RezervaceProhlidkyID BETWEEN 4 AND 7;

--13  Vypíše prùmernou cenu všech BMW v bazaru
SELECT TabulkaVozidel.Znacka, AVG(Cena) as cenaBMW FROM TabulkaVozidel  WHERE TabulkaVozidel.Znacka like 'BMW' GROUP BY TabulkaVozidel.Znacka;

--14 Zobrazí hezky èitelné datum vyrobených znaèek aut, které byly vyrobeny v CZ a seøadí je podle abecedy

SELECT TabulkaVozidel.Znacka, FORMAT (DatumVyroby,'dd MMMM, yyyy', 'cs-CZ') as DatumVyroby, ZemePuvodu FROM TabulkaVozidel WHERE ZemePuvodu like 'Èes%'
AND ( DatumVyroby is not NULL or DatumVyroby != ' ') ORDER BY Znacka;


--15 Vypiste vsechny VOZIDLA a jejich znacky a k nim vsechny modely jejichz cena je mezi 10tis.-400tis. a serad je podle abecedy 
SELECT (SELECT Znacka.Nazev FROM Znacka WHERE Model.ZnackaID = Znacka.ZnackaID) Znacka, Model.NazevModelu FROM Model
 JOIN Vozidlo ON Vozidlo.ModelID = Model.ModelID WHERE Cena BETWEEN 10000 and 400000 ORDER BY Znacka;

--16 NEJLEVNEJSI A NEJDRAZSI AUTO

select TabulkaVozidel.Znacka, cena FROM TabulkaVozidel where Cena = (SELECT MAX(CENA) as cena FROM TabulkaVozidel);
select TabulkaVozidel.Znacka, cena FROM TabulkaVozidel where Cena = (SELECT MIN(CENA) as cena FROM TabulkaVozidel);



--17 NAPIS MI, JAKA AUTA JSOU A JAKA AUTA NEJSOU K DISPOZICI a kdy a nahoru mi vyhod a serad rezervace od NEJDRIVEJSI :]

SELECT t.AutoID, t.Znacka, t.Model,r.DatumRezervace, StavDispozice = CASE
	WHEN RezervaceProhlidkyID is NULL then 'Neni k dispozici'
	ELSE 'Je dostupne'
END
FROM TabulkaVozidel t LEFT JOIN RezervaceProhlidky r ON r.AutoID = t.AutoID 
ORDER BY CASE WHEN DatumRezervace IS NULL THEN 1 ELSE 0 END, DatumRezervace ;






 