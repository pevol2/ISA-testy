Testy se spouští příkazem: 

sudo python3 test_X.py 		X je číslo testu

Výstupy se mohou lišit v IP adrese a přiřazeném portu v závislosti na testovaném zařízení. Testy fungují tak, že při spuštění testu se pošle daný paket. Uvnitř každého textového souboru jsou data obsažená v daném paketu. Výstupy se tedy porovnávají ručně.
Pozn. před spuštěním testu a odeslání paketu musí být spuštěn dns-monitor v druhém terminálu. 