import copy
import math
import stack

class PathFinder:
    def __init__(self):
        self.solved = []

    def find(self, s_x, s_y, e_x, e_y, labyrinth):
        self.solved = copy.deepcopy(labyrinth)
        x = s_x
        y = s_y
        cross_road = stack.Stack()
        path_points = stack.Stack()

        i = 0
        t = [0]

        while x != e_x or y != e_y:
            dir = self.avaliable_direction(x, y)
            if len(dir) == 1:
                x += dir[0][0]
                y += dir[0][1]

                path_points.push(x, y)
                self.solved[y][x] = 'x'
                t[i] += 1

            elif len(dir) > 1:
                n_x, n_y = self.find_best_distance(dir, x, y, e_x, e_y)
                cross_road.push(x, y)
                x = n_x
                y = n_y

                path_points.push(x, y)
                self.solved[y][x] = 'x'

                t.append(1)
                i+= 1

            else:
                ret = cross_road.pop()
                if len(ret) == 1:
                    break
                else:
                    x, y = ret
                    for m in range(t[i]):
                        path_points.pop()
                    del t[i]
                    i -= 1

        while path_points.size() > 0:
            x, y = path_points.pop()
            self.solved[y][x] = 'o'

        self.solved[e_y][e_x] = 'E'

        return self.solved

    def avaliable_direction(self, x, y):
        # 1 - left, 2 -right, 3 - up, 4 - down
        dir = []
        if self.solved[y][x - 1] in [' ', 'E']:
            dir.append((-1, 0))
        if self.solved[y][x + 1] in [' ', 'E']:
            dir.append((1, 0))
        if self.solved[y - 1][x] in [' ', 'E']:
            dir.append((0, -1))
        if self.solved[y + 1][x] in [' ', 'E']:
            dir.append((0, 1))
        return dir

    def check_distance(self, x, y, e_x, e_y):
        return abs(math.sqrt( (x - e_x) * (x - e_x) + (y - e_y) * (y - e_y)))

    def find_best_distance(self, dir, x, y, e_x, e_y):
        best_distance = []
        for d in dir:
            n_x = x + d[0]
            n_y = y + d[1]
            best_distance.append((self.check_distance(n_x, n_y, e_x, e_y), (n_x, n_y)))

        min = 0
        for i in range(len(best_distance)):
            if best_distance[i] < best_distance[min]:
                min = i

        return best_distance[min][1]

    def merge_labyrinths_paths(self, lab_1, lab_2):
        for i in range(len(lab_1)):
            for j in range(len(lab_1[0])):
                if lab_2[i][j] == 'o':
                    lab_1[i][j] = 'o'
                elif lab_2[i][j] == 'x' and lab_1[i][j] == ' ':
                    lab_1[i][j] = 'x'
        return lab_1
