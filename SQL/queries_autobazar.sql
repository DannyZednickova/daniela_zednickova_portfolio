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


--3 Vyp�e po�et aut ka�d� zna�ky, kter� m� naftu
SELECT Znacka.Nazev, COUNT(PalivoID) as pocet FROM Znacka 
RIGHT JOIN Model ON Model.ZnackaID = Znacka.ZnackaID
LEFT JOIN Vozidlo ON Vozidlo.ModelID = Model.ModelID 
WHERE PalivoID in (SELECT PalivoID FROM Palivo WHERE Nazev like 'Nafta') GROUP BY Znacka.Nazev;


--4 Vybere zna�ky a model + motor aut ktera jsou rezervovan� na p��t� m�s�c
 SELECT DISTINCT TabulkaVozidel.Znacka, TabulkaVozidel.Model, TabulkaVozidel.Motorizace, tbl.pocetRezervaci FROM TabulkaVozidel
 JOIN (SELECT AutoID, COUNT(RezervaceProhlidkyID) as pocetRezervaci FROM RezervaceProhlidky GROUP BY AutoID) AS TBL ON tbl.AutoID = TabulkaVozidel.AutoID 
 LEFT JOIN RezervaceProhlidky ON RezervaceProhlidky.AutoID = TabulkaVozidel.AutoID
 WHERE DatumRezervace < GETDATE()+30;
  


-- JEDNA DVOUSLOUPECKOVA TABULKA : SELECT AutoID, COUNT(RezervaceProhlidkyID) as pocet FROM RezervaceProhlidky GROUP BY AutoID;

SELECT Znacka.Nazev, Vozidlo.AutoID FROM Znacka 
JOIN Model ON Znacka.ZnackaID = Model.ZnackaID 
JOIN Vozidlo ON Vozidlo.ModelID = Model.ModelID

--- DRUHA DVOUSLOUPECKOVA TABULKA: (SELECT AutoID, COUNT(RezervaceProhlidkyID) as pocetRezervaci FROM RezervaceProhlidky GROUP BY AutoID)



--5 Zobraz� v�echna auta (model, zna�ku, motor a zem� p�vodu), kter� pochaz� z �eska a maj� vytvo�enou rezervaci 

SELECT Znacka.Nazev, Model.NazevModelu, Vozidlo.Motor, ZemePuvodu.NazevZeme FROM Znacka 
JOIN Model ON Znacka.ZnackaID = Model.ZnackaID
JOIN Vozidlo ON Vozidlo.ModelID= Model.ModelID
LEFT JOIN ZemePuvodu ON ZemePuvodu.ZemePuvoduID = Vozidlo.ZemePuvoduID
WHERE AutoID IN (SELECT DISTINCT AutoID FROM RezervaceProhlidky) AND ZemePuvodu.NazevZeme LIKE '�esk�%';



--6 Vypi�te zna�ky aut a jejich pr�m�rnou cenu ka�d� zna�ky 
SELECT Tabulkavozidel.Znacka, AVG(TabulkaVozidel.Cena) as PrumernaCena FROM TabulkaVozidel GROUP BY Tabulkavozidel.Znacka;


--7 Vypi�te po�et z�kazn�k�, kte�� si rezervovali benz�nov� auta
SELECT TabulkaVozidel.Palivo, COUNT(Zakaznik.ZakaznikID) as pocetZakazniku FROM TabulkaVozidel
 JOIN RezervaceProhlidky ON RezervaceProhlidky.AutoID = TabulkaVozidel.AutoID
 LEFT JOIN Zakaznik ON Zakaznik.ZakaznikID = RezervaceProhlidky.ZakaznikID WHERE TabulkaVozidel.Palivo like 'Benz�n' GROUP BY TabulkaVozidel.Palivo;

--8 Vypi�te nejstar�� auto  na sklad� 
SELECT Znacka, Model, Motorizace, DatumVyroby FROM TabulkaVozidel WHERE DatumVyroby <= (SELECT MIN(DatumVyroby) FROM TabulkaVozidel) ;

--9 Vypi�te 5 nejmlad��ch nerezervovan�ch aut

SELECT TOP 5 Znacka, DatumVyroby FROM TabulkaVozidel 
WHERE TabulkaVozidel.AutoID NOT IN (SELECT AutoID FROM RezervaceProhlidky )
ORDER BY DatumVyroby DESC;


--10 Vypi�te po�et v�ech nerezervovan�ch aut (Zna�ka, model, motorizace JE u aut VYPSAN� ) + vypsat na potvrzen�, �e maj� opravdu maji nulu :] 
SELECT TabulkaVozidel.Znacka , TabulkaVozidel.Model, TabulkaVozidel.Motorizace, COUNT (RezervaceProhlidkyID) as rezervace FROM TabulkaVozidel 
left JOIN RezervaceProhlidky ON TabulkaVozidel.AutoID = RezervaceProhlidky.AutoID 
WHERE RezervaceProhlidkyID is NULL OR RezervaceProhlidkyID = '' 
GROUP BY TabulkaVozidel.Znacka, TabulkaVozidel.Model, TabulkaVozidel.Motorizace HAVING Motorizace != '' and Motorizace is not null;

--11 Smazat auta, kter� nemaj� vyupln�nou ��dnou zna�ku �i model
DELETE FROM Vozidlo WHERE ModelID IS NULL or ModelID  = ' ';

-- 12 Nastav� datum vlo�en� aut, kter� nemaj� ID 1 a nastav� datum v�roby u aut, kter� maj� model vozida Octavia
UPDATE Vozidlo SET DatumVlozeni  = DATEADD(YEAR,-5, GETDATE() ) WHERE AutoID != 1;
UPDATE Vozidlo SET Vozidlo.DatumVyroby  = '2000-10-09' FROM Vozidlo
LEFT JOIN Model ON Model.ModelID = Vozidlo.ModelID WHERE Model.NazevModelu = 'Octavia';


--12 Smazat Rezervace jejich� ID je mezi 4 a 7
DELETE FROM RezervaceProhlidky WHERE RezervaceProhlidkyID BETWEEN 4 AND 7;

--13  Vyp�e pr�mernou cenu v�ech BMW v bazaru
SELECT TabulkaVozidel.Znacka, AVG(Cena) as cenaBMW FROM TabulkaVozidel  WHERE TabulkaVozidel.Znacka like 'BMW' GROUP BY TabulkaVozidel.Znacka;

--14 Zobraz� hezky �iteln� datum vyroben�ch zna�ek aut, kter� byly vyrobeny v CZ a se�ad� je podle abecedy

SELECT TabulkaVozidel.Znacka, FORMAT (DatumVyroby,'dd MMMM, yyyy', 'cs-CZ') as DatumVyroby, ZemePuvodu FROM TabulkaVozidel WHERE ZemePuvodu like '�es%'
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






 