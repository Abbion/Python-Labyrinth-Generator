import stack
import random


class Generator:
    def set_up_generator(self, x: int, y: int):
        self.size_x = x
        self.size_y = y

    def clear(self):
        #Tworzy siatkę dla labiryntu
        r_x = self.size_x
        if r_x % 2 == 0:
            r_x += 1

        r_y = self.size_y
        if r_y % 2 == 0:
            r_y += 1

        self.labyrinth = [ ['█' for i in range(r_x)] if j % 2 == 0 else ['█' if i % 2 == 0 else ' ' for i in range(r_x)] for j in range(r_y)]
        #LC

    def get_labyrinth(self):
        return self.labyrinth

    def generate(self, s_x: int, s_y: int, e_x: int, e_y: int):
        visited = 0
        x = int(self.size_x / 2)
        y = int(self.size_y / 2)

        self.bounds = (0, 0, x - 1, y - 1)
        self.grid = [[False for i in range(x)] for j in range(y)] #LC
        self.stack = stack.Stack()

        pos_x = s_x
        pos_y = s_y

        self.grid[pos_y][pos_x] = True
        self.stack.push(pos_x, pos_y)
        visited += 1

        #Do puki wszystkie punkty nie zostaną odwiedzone
        while visited < x * y:
            #wybierz kierunek
            direction = self.__random_dir(pos_x, pos_y)
            #Jeśli nie da się wybrać lub natrafiliśmy na punkt końcowy
            while direction == 0 or (pos_x == e_x and pos_y == e_y):
                pos = self.stack.pop()
                if len(pos) < 2:
                    break
                pos_x, pos_y = pos
                direction = self.__random_dir(pos_x, pos_y)

            #odkodowanie kierunku
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

            self.grid[new_y][new_x] = True
            self.stack.push(new_x, new_y)
            visited += 1

            self.labyrinth[1 + (pos_y * 2) + dir_y][1 + (pos_x * 2) + dir_x] = ' '

            pos_x = new_x
            pos_y = new_y

        #oznaczenie końca i początku labiryntu
        self.labyrinth[1 + s_y * 2][1 + s_x * 2] = 'S'
        self.labyrinth[1 + e_y * 2][1 + e_x * 2] = 'E'
        #sprawdzenie czy linia prosta nie łączy wejścia i wyjścia
        self.__line_test(1 + s_x * 2, 1 + s_y * 2, 1 + e_x * 2, 1 + e_y * 2)

    def __random_dir(self, x: int, y: int):
        #wybiera lowoy kierunek
        # 1 - left, 2 -right, 3 - up, 4 - down
        dir = []

        if x != 0:
            if not self.grid[y][x - 1]:
                dir.append(1)
        if x != self.bounds[2]:
            if not self.grid[y][x + 1]:
                dir.append(2)
        if y != 0:
            if not self.grid[y - 1][x]:
                dir.append(3)
        if y != self.bounds[3]:
            if not self.grid[y + 1][x]:
                dir.append(4)

        if len(dir) == 0:
            return 0
        else:
            return random.choice(dir)

    def __line_test(self, s_x, s_y, e_x, e_y):
        #testuje czy start nie łączy koniec linia prosta
        #jeśli istnieje linia prosta na osi X
        if s_x == e_x:
            #Jeśli start jest wyżej od końca
            if s_y > e_y:
                for i in range(1, (s_y - e_y)):
                    if self.labyrinth[s_y - i][s_x] == '█':
                        return
                self.labyrinth[e_y + 1][e_x] = '█'

                if e_y > 1:
                    self.labyrinth[e_y - 1][e_x] = ' '
                    return
                if e_x > 1:
                    self.labyrinth[e_y][e_x - 1] = ' '
                    return
                else:
                    self.labyrinth[e_y][e_x + 1] = ' '
                    return

            #Jeśli start jest niżej od końca
            else:
                for i in range(1, (e_y - s_y)):
                    if self.labyrinth[s_y + i][s_x] == '█':
                        return
                self.labyrinth[e_y - 1][e_x] = '█'

                if e_y < self.bounds[3] * 2 + 1:
                    self.labyrinth[e_y + 1][e_x] = ' '
                    return
                if e_x == 1:
                    self.labyrinth[e_y][e_x + 1] = ' '
                    return
                else:
                    self.labyrinth[e_y][e_x - 1] = ' '
                    return

        # jeśli istnieje linia prosta na osi Y
        elif s_y == e_y:
            #jeśli start leży na prawo od końca
            if s_x > e_x:
                for i in range(1, (s_x - e_x)):
                    if self.labyrinth[s_y][s_x - i] == '█':
                        return
                self.labyrinth[s_y][e_x + 1] = '█'

                if e_x > 1:
                    self.labyrinth[e_y][e_x - 1] = ' '
                    return
                if e_y > 1:
                    self.labyrinth[e_y - 1][e_x] = ' '
                    return
                else:
                    self.labyrinth[e_y + 1][e_x] = ' '
                    return
            #jeśli start leży na lewo od końca
            else:
                for i in range(1, (e_x - s_x)):
                    if self.labyrinth[s_y][s_x + i] == '█':
                        return
                self.labyrinth[s_y][e_x - 1] = '█'

                if e_y > 1:
                    self.labyrinth[e_y - 1][e_x] = ' '
                    return
                if e_x == 1 + self.bounds[2] * 2:
                    self.labyrinth[e_y + 1][e_x] = ' '
                    return
                else:
                    self.labyrinth[e_y][e_x + 1] = ' '
                    return
