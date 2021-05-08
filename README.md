# Generator labiryntów
### Opis zadania
* Główne okno programu zawiera kontrolki pozwalające na wybór wielkości labiryntu (liczba pól N na M; para liczb całkowitych nie większych niż 30), wizualizację labiryntu (na przykład jako siatka kolorowych przycisków) oraz przycisk "generuj".

* Labirynt składa się z pól będących korytarzem lub ścianą.

* Użytkownik wybiera dwa różne pola będące wejściem i wyjściem. Pola te traktowane będą jak korytarz. Po naciśnięciu przycisku "generuj” następuje generowanie losowego labiryntu.

* Dla każdej pary pól będących korytarzem powinna istnieć ścieżka je łącząca (brak pól odłączonych od reszty labiryntu). Przechodzenie możliwe jest tylko na pola będące korytarzem które sąsiadują krawędzią z danym polem. Wygenerowany labirynt powinien posiadać ścieżkę od wejścia do wyjścia, która nie będzie linią prostą (poziomą lub pionową) i która powinna być zaznaczona na wizualizacji.

* Przechowywana jest lista punktów pośrednich ścieżki prowadzącej od wejścia do wyjścia.

* Po wybraniu dowolnego pola będącego korytarzem, dodawane jest ono na koniec listy punktów pośrednich. Następnie powinna zostać znaleziona i zaznaczona najkrótsza ścieżka prowadząca z wejścia do wyjścia przez wszystkie punkty pośrednie.

* Wybranie pola będącego punktem pośrednim powoduje usunięcie danego punktu pośredniego.

* Labirynt nie może posiadać żadnego 'pokoju': obszar 2 na 2 pola korytarza (lub większy).

* Labirynt nie może posiadać żadnych obszarów 3 na 3 pola ściany (lub większych).
