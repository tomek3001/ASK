
# Dokumentacja projektu 5

Wykonawcy:
**Jakub Osielski 171973**
**Tomasz Szymañski 160286**


## Polecenie
Tematem zadania pi¹tego jest napisanie aplikacji uzale¿nionej od czasu. Jednym z zadañ aplikacji ma byæ mo¿liwie precyzyjny pomiar lub odmierzanie czasu. Wykorzystuj¹c dowolny jêzyk programowania dla omputerów w standardzie PC napisaæ aplikacjê spe³niaj¹c¹ funkcjê testera sprawnoœci psychomotorycznej np. kandydatów na kierowców. Na aplikacjê powinna siê sk³adaæ seria ró¿nych testów badaj¹cych prosty i ³o¿ony czas reakcji na bodŸce optyczne i akustyczne. Ka¿dy test w³aœciwy powinna poprzedzaæ informacja o przebiegu testu oraz faza szkoleniowa, w trakcie której osoba badana wykona te same czynnoœci co w trakcie testu, ale bez oceny. Po wykonaniu serii testów osoba poddana badaniom powinien zostaæ poinformowana o osi¹gniêtych wynikach w formie syntetycznej i analitycznej z wykorzystaniem wartoœci liczbowych i reprezentacji graficznej.

Opracowanemu programowi powinna towarzyszyæ dokumentacja – sprawozdanie. Sprawozdanie powinno zawieraæ:
- sformu³owanie zadania wraz z przyjêciem za³o¿eñ szczegó³owych np. sposobu pomiaru czasu i okreœlania interwa³ów czasowych;  
- opis przyjêtych rozwi¹zañ programowych zilustrowanych ewentualnie fragmentami kodu (nie zamieszczaæ wydruków ca³ych programów!);
- dyskusjê osi¹gniêtych wyników z wskazaniem wad i zalet napisanej aplikacji.

## Za³o¿enia projektowe

Stworzenie prostej aplikacji testuj¹cej czas reakcji z dwoma trybami: treningowym i testowym.

## Realizacja

Do realizacji za³o¿onych celów wykorzystany zosta³ jêzyk Python wraz z dodatkowymi bibliotekami, a interfejs stworzyliœmy przy wykorzystaniu PySide2.
Program posiada menu z opcjami testu i treningu. Po treningu ekran powraca do menu g³ównego. Po teœcie program ulega zamkniêciu.

### Opcja treningu
W opcji treningowej mo¿liwe jest æwiczenie ka¿dego zadania bez limitu czasowego. Przejœcie do kolejnego zadania odbywa siê poprzez wciœniêcie klawisza litery "c".
### Opcja testu
Wyniki testu wyœwietlane s¹ na bie¿¹co, a dodatkowo na sam koniec wyœwietlana jest graficzna interpretacja wyników pierwszego testu. Zadania prze³¹czane s¹ automatycznie.
### Pomiar czasu
Pomiar czasu odbywa siê poprzez pobranie aktualnej godziny wraz z rozpoczêciem jego zliczania i przypisanie jej do zmiennej start. Po zakoñczeniu mierzonego zadania wartoœæ zmiennej tej odejmowana jest od aktualnego czasu. Ró¿nica miêdzy tymi dwoma wartoœciami mówi nam o tym ile czasu up³ynê³o.

## Podsumowanie, uwagi

Program, mimo swojej prostoty, spe³nia za³o¿enia projektowe.

### Zalety
- Testy oparte na czasie
- Szybkoœæ dzia³ania
- Opcja treningowa i testowa

### Wady
- Niezbyt rozbudowana analiza danych
- Brak mo¿liwoœci porównania wyników z wynikami innych