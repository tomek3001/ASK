
# Dokumentacja projektu 5

Wykonawcy:
**Jakub Osielski 171973**
**Tomasz Szyma�ski 160286**


## Polecenie
Tematem zadania pi�tego jest napisanie aplikacji uzale�nionej od czasu. Jednym z zada� aplikacji ma by� mo�liwie precyzyjny pomiar lub odmierzanie czasu. Wykorzystuj�c dowolny j�zyk programowania dla omputer�w w standardzie PC napisa� aplikacj� spe�niaj�c� funkcj� testera sprawno�ci psychomotorycznej np. kandydat�w na kierowc�w. Na aplikacj� powinna si� sk�ada� seria r�nych test�w badaj�cych prosty i �o�ony czas reakcji na bod�ce optyczne i akustyczne. Ka�dy test w�a�ciwy powinna poprzedza� informacja o przebiegu testu oraz faza szkoleniowa, w trakcie kt�rej osoba badana wykona te same czynno�ci co w trakcie testu, ale bez oceny. Po wykonaniu serii test�w osoba poddana badaniom powinien zosta� poinformowana o osi�gni�tych wynikach w formie syntetycznej i analitycznej z wykorzystaniem warto�ci liczbowych i reprezentacji graficznej.

Opracowanemu programowi powinna towarzyszy� dokumentacja � sprawozdanie. Sprawozdanie powinno zawiera�:
- sformu�owanie zadania wraz z przyj�ciem za�o�e� szczeg�owych np. sposobu pomiaru czasu i okre�lania interwa��w czasowych;  
- opis przyj�tych rozwi�za� programowych zilustrowanych ewentualnie fragmentami kodu (nie zamieszcza� wydruk�w ca�ych program�w!);
- dyskusj� osi�gni�tych wynik�w z wskazaniem wad i zalet napisanej aplikacji.

## Za�o�enia projektowe

Stworzenie prostej aplikacji testuj�cej czas reakcji z dwoma trybami: treningowym i testowym.

## Realizacja

Do realizacji za�o�onych cel�w wykorzystany zosta� j�zyk Python wraz z dodatkowymi bibliotekami, a interfejs stworzyli�my przy wykorzystaniu PySide2.
Program posiada menu z opcjami testu i treningu. Po treningu ekran powraca do menu g��wnego. Po te�cie program ulega zamkni�ciu.

### Opcja treningu
W opcji treningowej mo�liwe jest �wiczenie ka�dego zadania bez limitu czasowego. Przej�cie do kolejnego zadania odbywa si� poprzez wci�ni�cie klawisza litery "c".
### Opcja testu
Wyniki testu wy�wietlane s� na bie��co, a dodatkowo na sam koniec wy�wietlana jest graficzna interpretacja wynik�w pierwszego testu. Zadania prze��czane s� automatycznie.
### Pomiar czasu
Pomiar czasu odbywa si� poprzez pobranie aktualnej godziny wraz z rozpocz�ciem jego zliczania i przypisanie jej do zmiennej start. Po zako�czeniu mierzonego zadania warto�� zmiennej tej odejmowana jest od aktualnego czasu. R�nica mi�dzy tymi dwoma warto�ciami m�wi nam o tym ile czasu up�yn�o.

## Podsumowanie, uwagi

Program, mimo swojej prostoty, spe�nia za�o�enia projektowe.

### Zalety
- Testy oparte na czasie
- Szybko�� dzia�ania
- Opcja treningowa i testowa

### Wady
- Niezbyt rozbudowana analiza danych
- Brak mo�liwo�ci por�wnania wynik�w z wynikami innych