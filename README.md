# ASK Zadanie 4


## Polecenie


Tematem zadania czwartego jest wykorzystanie interfejsów dostępnych w komputerze PC do komunikacji pomiędzy dwoma  
komputerami. Wykorzystując dowolnie wybrany język programowania napisać aplikację symulującą transmisję szeregową zgodną ze  
standardem RS232. W oknie nadajnika przygotowujemy tekst do nadania w postaci ciągu znaków ASCII. Następnie tekst ten jest  
formatowany do formatu bit startu, bity znaku od LSB do MSB i dwa bity stopu i zapisywany do łańcucha (każdy znak ASCII  
posiada własny bit startu i bity stopu!!!). Łańcuch powinien zostać wyświetlony w osobnym polu na ekranie. Następnie łańcuch jest  
przesyłany do odbiornika, którym może być drugie okno tego samego programu, drugi program lub nawet inne pole panelu tego  
samego programu. Jako nośnika danych można użyć: tablicy (gdy nadajnik i odbiornik są w tym samym programie), pliku lub  
wybranego protokołu komunikacyjnego np. TCP/IP – przy czym pierwsze dwie metody są wystarczające. W odbiorniku łańcuch  
danych zostaje poddany dekodowaniu, tj. usunięciu ramek i dekompozycji szeregowo równoległej. Tekst po zamianie na ciąg znaków  
ASCII powinien zostać wyświetlony w oddzielnym polu. Elementem aplikacji powinna być również dbałość o czystość języka.  
Należy to zrealizować w postaci słownika „grubiaństw” zawartego w osobnym pliku. Napotkanie w nadawanym lub odbieranym  
tekście „grubego” słowa ze słownika powinno skutkować zastąpieniem wszystkich jego liter ciągiem gwiazdek.

Opracowanemu programowi powinna towarzyszyć dokumentacja – sprawozdanie. Sprawozdanie powinno zawierać:  
- sformułowanie zadania wraz z przyjęciem założeń szczegółowych np. zasad przekazywania informacji pomiędzy nadajnikiem i  
odbiornikiem, konwersji znak ASCII <->strumień bitów, mechanizmów stosowania filtracji „niecenzuralnych” słów;  
- opis przyjętych rozwiązań programowych zilustrowanych ewentualnie fragmentami kodu (nie zamieszczać wydruków całych  
programów!);  
- dyskusję osiągniętych wyników z wskazaniem wad i zalet napisanej aplikacji.

