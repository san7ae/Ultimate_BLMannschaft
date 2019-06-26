SELECT Name, Verein, Position, Tore*4, Vorlagen*3, ShotOnTarget, TorschussVorlagen*0.5, ((Tore*4)+(Vorlagen*3)+ShotOnTarget+(TorschussVorlagen*0.5))  as Rating
FROM `database`.spieler
WHERE Position = "Stürmer" OR Position = "Mittelstürmer"
ORDER BY Rating DESC LIMIT 3;


SELECT Name, Verein, Position, Tore*4, Vorlagen*3, ShotOnTarget, TorschussVorlagen*0.5, ((Tore*4)+(Vorlagen*3)+ShotOnTarget+(TorschussVorlagen*0.5))  as Rating
FROM `database`.spieler
WHERE Position = "Linke Außenbahn" OR Position = "Linksaußen"
ORDER BY Rating DESC LIMIT 2;


SELECT Name, Verein, Position, Tore*4, Vorlagen*3, ShotOnTarget, TorschussVorlagen*0.5, ((Tore*4)+(Vorlagen*3)+ShotOnTarget+(TorschussVorlagen*0.5))  as Rating
FROM `database`.spieler
WHERE Position = "Rechte Außenbahn" OR Position = "Rechtsaußen"
ORDER BY Rating DESC LIMIT 2;


SELECT Name, Verein, CleanSheet, Paraden/10, AbgewehrteElfmeter/GesamteElfmeter*10, (CleanSheet+(Paraden/10)+(AbgewehrteElfmeter/GesamteElfmeter*10))  as Rating
FROM `database`.spieler
WHERE Position = "Torhüter"
ORDER BY Rating DESC  LIMIT 3;


SELECT Name, Verein, Position,  (((SuccessfulDribblings/TotalDribblings) * 10) + (( PassCompleted/ TotalPass) * 10) + (GrosschancenKreiert /2) + (Tore * 4)  + (Vorlagen * 3) +(ShotOnTarget / 10) + (TorschussVorlagen /10)) as Rating
FROM `database`.spieler
WHERE Position = "Zentrales Mittelfeld"
ORDER BY Rating DESC LIMIT 2;


SELECT Name, Verein, Position,  (((SuccessfulDribblings/TotalDribblings) * 10) + (( PassCompleted/ TotalPass) * 10) + (GrosschancenKreiert /2) + (Tore * 4)  + (Vorlagen * 3) +(ShotOnTarget / 10) + (TorschussVorlagen /10)) as Rating
FROM `database`.spieler
WHERE Position = "Defensives Mittelfeld"
ORDER BY Rating DESC LIMIT 2;



SELECT Name, Verein, Position,  (((SuccessfulDribblings/TotalDribblings) * 10) + (( PassCompleted/ TotalPass) * 10) + (GrosschancenKreiert /2) + (Tore * 4)  + (Vorlagen * 3) +(ShotOnTarget / 10) + (TorschussVorlagen /10)) as Rating
FROM `database`.spieler
WHERE Position = "Offensives Mittelfeld"
ORDER BY Rating DESC LIMIT 2;



SELECT Name, Verein, Position, ((GewonneneLuftkaempfe/GesamteLuftkaempfe) +
(GewonneneZweikaempfe/GesamteZweikaempfe) + ((PassCompleted/ TotalPass) * 10) + (AbgefangeneBaelle/10) + (GeklaerteBaelle/20 ) + ((SuccessfulTackles / TotalTackles) * 10)) as Rating
FROM `database`.spieler
WHERE Position = "Linksverteidiger"
ORDER BY Rating DESC LIMIT 2;



SELECT Name, Verein, Position, Tore, Vorlagen, ((GewonneneLuftkaempfe/GesamteLuftkaempfe) +
(GewonneneZweikaempfe/GesamteZweikaempfe) + ((PassCompleted/ TotalPass) * 10) + (AbgefangeneBaelle/10) + (GeklaerteBaelle/20 ) + ((SuccessfulTackles / TotalTackles) * 10)) +(Tore * 4) + (Vorlagen * 3) as Rating
FROM `database`.spieler
WHERE Position = "Rechtsverteidiger"
ORDER BY Rating DESC LIMIT 2;



SELECT Name, Verein, Position, Tore, Vorlagen, ((GewonneneLuftkaempfe/GesamteLuftkaempfe) +
(GewonneneZweikaempfe/GesamteZweikaempfe) + ((PassCompleted/ TotalPass) * 10) + (AbgefangeneBaelle/10) + (GeklaerteBaelle/20 ) + ((SuccessfulTackles / TotalTackles) * 10)) +(Tore * 4) + (Vorlagen * 3) as Rating
FROM `database`.spieler
WHERE Position = "Innenverteidiger"
ORDER BY Rating DESC LIMIT 4;


