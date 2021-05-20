import stack
import random


class Generator:
    def set_up_generator(self, x: int, y: int):
        self.size_x = x
        self.size_y = y

    def clear(self):
        r_x = self.size_x
        if r_x % 2 == 0:
            r_x += 1

        r_y = self.size_y
        if r_y % 2 == 0:
            r_y += 1

        self.labyrinth = []
        for i in range(r_y):
            row = []
            for j in range(r_x):
                if i % 2 == 0 or j % 2 == 0:
                    row.append('█')
                else:
                    row.append(' ')
            self.labyrinth.append(row)

    def get_labyrinth(self):
        return self.labyrinth



    def generate(self, s_x : int, s_y : int, e_x : int, e_y : int):
        visited = 0
        x = int(self.size_x / 2)
        y = int(self.size_y / 2)

        self.bounds = (0, 0, x - 1, y - 1)
        self.grid = [[False for i in range(x)] for j in range(y)]
        self.stack = stack.stack()

        posX = s_x
        posY = s_y

        self.grid[posY][posX] = True
        self.stack.push(posX, posY)
        visited += 1

        while visited < x * y:
            direction = self.random_dir(posX, posY)
            while direction == 0 or (posX == e_x and posY == e_y):
                pos = self.stack.pop()
                if len(pos) < 2:
                    break
                posX, posY = pos
                direction = self.random_dir(posX, posY)

            dirX = 0
            dirY = 0

            if direction != 0:
                if direction == 1:
                    dirX = -1
                elif direction == 2:
                    dirX = 1
                elif direction == 3:
                    dirY = -1
                elif direction == 4:
                    dirY = 1

                newX = posX + dirX
                newY = posY + dirY

                self.grid[newY][newX] = True
                self.stack.push(newX, newY)
                visited += 1

                #self.labyrinth[1 + (posX * 2) + dirX ][1 + (posY * 2) + dirY] = ' '
                #print('y: ', 1 + (posY * 2), ' x: ', 1 + (posX * 2) + dirX)
                self.labyrinth[1 + (posY * 2) + dirY][1 + (posX * 2) + dirX] = ' '


                posX = newX
                posY = newY
                #print("v ", visited, " dir ", direction, " x: ", posX, " y: ", posY)

        self.labyrinth[1 + s_y * 2][1 + s_x * 2] = 'S'
        self.labyrinth[1 + e_y * 2][1 + e_x * 2] = 'E'
        self.line_test(1 + s_x * 2, 1 + s_y * 2, 1 + e_x * 2, 1 + e_y * 2)


    def random_dir(self, x: int, y: int):
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

    def line_test(self, s_x, s_y, e_x, e_y):
        if s_x == e_x:
            if s_y > e_y:
                for i in range(1, (s_y - e_y)):
                    if self.labyrinth[s_y-i][s_x] == '█':
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

            if s_y < e_y:
                for i in range(1, (e_y - s_y)):
                    if self.labyrinth[s_y + i][s_x] == '█':
                        return
                self.labyrinth[e_y - 1][e_x] = '█'
                print('FOUND')

                if e_y < self.bounds[3] * 2 + 1:
                    self.labyrinth[e_y + 1][e_x] = ' '
                    return
                if e_x == 1:
                    self.labyrinth[e_y][e_x + 1] = ' '
                    return
                else:
                    self.labyrinth[e_y][e_x - 1] = ' '
                    return



        elif s_y == e_y:
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
            else:
                for i in range(1, (e_x - s_x)):
                    if self.labyrinth[s_y][s_x + i] == '█':
                        return
                self.labyrinth[s_y][e_x -1] = '█'
                if e_y > 1:
                    self.labyrinth[e_y - 1][e_x] = ' '
                    return
                if e_x == 1 + self.bounds[2] * 2:
                    self.labyrinth[e_y + 1][e_x] = ' '
                    return
                else:
                    self.labyrinth[e_y][e_x + 1] = ' '
                    return