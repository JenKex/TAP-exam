# TAP-exam

1) Vad jag har testat
Jag har testat steps för feature-filerna, inklusive: Att se hela listan av tillgängliga böcker, att lägga till nya böcker, att lägga till favoriter och se dem i ens lista favoriter, att ta bort favoritmarkerade böcker och se dem försvinna från ens lista favoriter, och att se totalmängden användare och deras favoritmarkerade böcker. Jag har också kört enhetstester och integrationstester för backend (att lägga till böcker i en bookStore-lista, att toggla favoriter och att kunna lägga till/ta bort böcker från en lista favoriter).

2) Projektet klonas ner till en passande mapp. Behave-tester körs via `behave` i terminalen och backend-tester körs via `pytest`, med alternativen att köra antingen `pytest -m unit` för enhetstester eller `pytest -m integration` för integrationstester.