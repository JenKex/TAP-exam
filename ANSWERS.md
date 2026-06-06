<!-- 1: Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest? -->

Enhetstest testar en funktion eller metod åt gången för att se om en feature funkar i grunden.
Integrationstest testar flera funktioner eller metoder i kombination. Detta hjälper till att visa om någonting går sönder när flera faktorer är inblandade, och simulerar buggar som kan dyka upp från naturligt användarbeteende (t.ex. att använda flera features efter varandra på en app eller webbsajt).
Regressionstest testar för om funktioner som tidigare fungerade fortfarande funkar, i och med att nyintroducerade funktioner kan leda till nya fel eller återintroducera gamla fel. Enhetstest blir naturligt till regressionstest i takt med att utveckling fortgår.
Prestandatest testar inte bara för ifall en funktion funkar, utan för hur snabb eller effektiv en funktion är i sin implementation. Med prestandatest kan en utvecklare testa flera olika upplägg för en metod för att se vilken som är snabbast.

<!-- 2: Beskriv hur det går till när man arbetar med TDD. -->

Man skriver test innan man bygger funktioner, kör testerna, får tillbaka röda testfall, skriver minst möjliga bit kod som får testfallen att returnera grönt, potentiellt refaktorerar (rensar upp/optimerar koden), skriver fler tester, och upprepar processen.
TDD hjälper en att fokusera på att se till att alla ens funktioner fungerar på en grundnivå, och att via metodisk testning se till att man inte saboterar ett gammalt testfall i ens implementering av en ny funktion.

<!-- 3: Beskriv hur BDD skiljer sig från TDD. -->

BDD -- Behavioral Driven Development -- grundar sig i att utforma testfall baserat på beteendet som man vill eftersträva med sin applikation. Det är ett utvecklingstänk som kan integrera flera olika roller i företaget/teamet genom att formulera sina testfall mer på en grundnivå av vad det eftersträvade resultatet är, på ett sätt som är lättare att förstå för icke-utvecklare och mer övergripande. (T.ex. 'Om jag har 100 kronor i mitt bankkonto, när jag sätter in 50 kronor till vill jag att det ska finnas 150 kronor i mitt bankkonto' snarare än 'Om det står '100' i total-fältet på bankkontot med användar-ID '1', och jag klickar på 'sätt in pengar'-fältet, och jag fyller i '50' i 'total mängd'-fältet...' o.s.v.)

BDD blir därför mer inriktat på storskaligt tänk och övergripande mål, medans TDD är mer inriktat på mikrotester och moment-till-moment-implementation av hur man uppnår dessa mål.

<!-- 4: Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val. -->

Jag skulle använda vissa enhetstest för att säkerställa basfunktionaliteten, men huvudsakligen använda mig av integrationstest. Grundfunktionerna är såpass enkla att man inte behöver skriva särskilt många enhetstest, och i och med att användarbeteende kan trigga oväntade buggar skulle jag fokusera mer på integrationstester och E2E. Jag skulle också använda prestandatest på vissa kärnfunktioner (t.ex. att lägga till böcker och returnera databasen) för att se till att de funktioner som är viktigast för sajtens grundfeatures körs snabbt och effektivt.

Jag skulle också använda mig av vissa icke-funktionella test -- t.ex. att ta in utomstående och få deras intryck -- för att se om frontenden är tydlig och användarvänlig.