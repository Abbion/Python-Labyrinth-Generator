import stack
import random


class Generator:
    """Klasa generująca labirynt"""
    def set_up_generator(self, x: int, y: int):
        self.__size_x = x
        self.__size_y = y

    def clear(self):
        #Tworzy siatkę dla labiryntu

        #Dostosowanie labiryntu do odpowiednich rozmiarów
        r_x = self.__size_x
        if r_x % 2 == 0:
            r_x += 1

        r_y = self.__size_y
        if r_y % 2 == 0:
            r_y += 1

        #list comprehension dla siatki
        self.__labyrinth = [['█' for i in range(r_x)] if j % 2 == 0 else ['█' if i % 2 == 0 else ' ' for i in range(r_x)] for j in range(r_y)]

    def get_labyrinth(self):
        return self.__labyrinth

    def generate(self, s_x: int, s_y: int, e_x: int, e_y: int):
        visited = 0
        x = int(self.__size_x / 2)
        y = int(self.__size_y / 2)

        #Ograniczenia i tworzenie siatki odwiedzin dla labiryntu
        self.__bounds = (0, 0, x - 1, y - 1)
        self.__grid = [[False for i in range(x)] for j in range(y)]
        self.__stack = stack.Stack()

        pos_x = s_x
        pos_y = s_y

        self.__grid[pos_y][pos_x] = True
        self.__stack.push(pos_x, pos_y)
        visited += 1

        #Dopóki wszystkie punkty nie zostaną odwiedzone
        while visited < x * y:
            #Wybierz kierunek
            direction = self.__random_dir(pos_x, pos_y)
            #Jeśli nie da się wybrać lub natrafiliśmy na punkt końcowy
            while direction == 0 or (pos_x == e_x and pos_y == e_y):
                pos = self.__stack.pop()
                if len(pos) < 2:
                    break
                pos_x, pos_y = pos
                direction = self.__random_dir(pos_x, pos_y)

            #Odkodowanie kierunku
            dir_x = 0
            dir_y = 0

            if direction == 1:
                dir_x = -1
            elif direction == 2:
                dir_x = 1
            elif direction == 3:
                dir_y = -1
            elif direction == 4:
                dir_y = 1

            new_x = pos_x + dir_x
            new_y = pos_y + dir_y

            self.__grid[new_y][new_x] = True
            self.__stack.push(new_x, new_y)
            visited += 1

            self.__labyrinth[1 + (pos_y * 2) + dir_y][1 + (pos_x * 2) + dir_x] = ' '

            pos_x = new_x
            pos_y = new_y

        #Oznaczenie końca i początku labiryntu
        self.__labyrinth[1 + s_y * 2][1 + s_x * 2] = 'S'
        self.__labyrinth[1 + e_y * 2][1 + e_x * 2] = 'E'
        #sprawdzenie, czy linia prosta nie łączy wejścia i wyjścia
        self.__line_test(1 + s_x * 2, 1 + s_y * 2, 1 + e_x * 2, 1 + e_y * 2)

    def __random_dir(self, x: int, y: int):
        #Wybiera losowy kierunek
        # 1 - left, 2 -right, 3 - up, 4 - down
        dir = []

        if x != 0:
            if not self.__grid[y][x - 1]:
                dir.append(1)
        if x != self.__bounds[2]:
            if not self.__grid[y][x + 1]:
                dir.append(2)
        if y != 0:
            if not self.__grid[y - 1][x]:
                dir.append(3)
        if y != self.__bounds[3]:
            if not self.__grid[y + 1][x]:
                dir.append(4)

        if len(dir) == 0:
            return 0
        else:
            return random.choice(dir)

    def __line_test(self, s_x, s_y, e_x, e_y):
        #Testuje czy start nie łączy koniec linia prosta
        #Jeśli istnieje linia prosta na osi X
        if s_x == e_x:
            #Jeśli start jest wyżej od końca
            if s_y > e_y:
                for i in range(1, (s_y - e_y)):
                    if self.__labyrinth[s_y - i][s_x] == '█':
                        return
                self.__labyrinth[e_y + 1][e_x] = '█'

                if e_y > 1:
                    self.__labyrinth[e_y - 1][e_x] = ' '
                    return
                if e_x > 1:
                    self.__labyrinth[e_y][e_x - 1] = ' '
                    return
                else:
                    self.__labyrinth[e_y][e_x + 1] = ' '
                    return

            #Jeśli start jest niżej od końca
            else:
                for i in range(1, (e_y - s_y)):
                    if self.__labyrinth[s_y + i][s_x] == '█':
                        return
                self.__labyrinth[e_y - 1][e_x] = '█'

                if e_y < self.__bounds[3] * 2 + 1:
                    self.__labyrinth[e_y + 1][e_x] = ' '
                    return
                if e_x == 1:
                    self.__labyrinth[e_y][e_x + 1] = ' '
                    return
                else:
                    self.__labyrinth[e_y][e_x - 1] = ' '
                    return

        #Jeśli istnieje linia prosta na osi Y
        elif s_y == e_y:
            #Jeśli start leży na prawo od końca
            if s_x > e_x:
                for i in range(1, (s_x - e_x)):
                    if self.__labyrinth[s_y][s_x - i] == '█':
                        return
                self.__labyrinth[s_y][e_x + 1] = '█'

                if e_x > 1:
                    self.__labyrinth[e_y][e_x - 1] = ' '
                    return
                if e_y > 1:
                    self.__labyrinth[e_y - 1][e_x] = ' '
                    return
                else:
                    self.__labyrinth[e_y + 1][e_x] = ' '
                    return
            #Jeśli start leży na lewo od końca
            else:
                for i in range(1, (e_x - s_x)):
                    if self.__labyrinth[s_y][s_x + i] == '█':
                        return
                self.__labyrinth[s_y][e_x - 1] = '█'

                if e_y > 1:
                    self.__labyrinth[e_y - 1][e_x] = ' '
                    return
                if e_x == 1 + self.__bounds[2] * 2:
                    self.__labyrinth[e_y + 1][e_x] = ' '
                    return
                else:
                    self.__labyrinth[e_y][e_x + 1] = ' '
                    return
