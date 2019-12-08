Wiadomości ogólne
Dokument dotyczy procesu przetwarzania i oczysczania danych dotyczących pogody (weather.txt). 


Wymagania
Do uruchomienia projektu konieczne jest posiadanie oprogramowania jupyter.


Etapy przetwarzania danych
I. Konwersja pliku weather.txt do formatu .csv, który mógł zostać wczytany przez funkcję DataFrame
Polega na zastąpieniu separatorów I i S znakiem ','. Dodatkowo pierwsza kolumna została podzielona na kolumny:
id, year, month oraz typ pomiaru

II. Wykonanie polecenia melt na DataFrame
Usuniete zostały kolumny z dniami. Utworzona została kolumna zawierająca datę dzienną

III. pivot
Wykonanie metody pivot na danych, tak, by dla każdego typu pomiaru (prcp, tmin, tmax) powstała osobna
kolumna.


