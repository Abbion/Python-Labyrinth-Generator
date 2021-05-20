import copy
import math
import stack

class PathFinder:
    def find(self, s_x, s_y, e_x, e_y, labyrinth):
        self.path_finder = copy.deepcopy(labyrinth)
        #self.solved = copy.deepcopy(labyrinth)
        path = self.find_path(s_x, s_y, e_x, e_y)
        #self.get_best(s_x, s_y, e_x, e_y, path)


        #path.print()
        self.path_finder[e_y][e_x] = 'E'
        return self.path_finder

    def avaliable_direction(self, x, y, check):
        # 1 - left, 2 -right, 3 - up, 4 - down
        dir = []
        if check[y][x - 1] in [' ', 'E']:
            dir.append((-1, 0))
        if check[y][x + 1] in [' ', 'E']:
            dir.append((1, 0))
        if check[y - 1][x] in [' ', 'E']:
            dir.append((0, -1))
        if check[y + 1][x] in [' ', 'E']:
            dir.append((0, 1))
        return dir

    def check_distance(self, x, y, e_x, e_y):
        return abs(math.sqrt(e_x * e_x + e_y * e_y) - math.sqrt(x * x + y * y))

    def find_best_distance(self, dir, x, y, e_x, e_y):
        best_distance = []
        for d in dir:
            n_x = x + d[0]
            n_y = y + d[1]
            best_distance.append((self.check_distance(n_x, n_y, e_x, e_y), (n_x, n_y)))

        min = 0
        for i in range(len(best_distance)):
            if best_distance[min] > best_distance[i]:
                min = i
        return best_distance[min][1], dir[min]

    def find_path(self, s_x, s_y, e_x, e_y):
        x = s_x
        y = s_y
        cross_road = stack.stack()

        while x != e_x or y != e_y:
            dir = self.avaliable_direction(x, y, self.path_finder)
            if len(dir) == 1:
                x += dir[0][0]
                y += dir[0][1]
                self.path_finder[y][x] = 'x'
            elif len(dir) > 1:

                n_xy, min_dir = self.find_best_distance(dir, x, y, e_x, e_y)
                cross_road.push((x, y), min_dir)
                x = n_xy[0]
                y = n_xy[1]
                self.path_finder[y][x] = 'x'
            else:
                ret = cross_road.pop()
                if len(ret) == 1:
                    break
                else:
                    x, y = ret[0]
        return cross_road

    def get_best(self, s_x, s_y, e_x, e_y, path):
        x = s_x
        y = s_y
        dir = self.avaliable_direction(x, y, self.solved)

        for pt in range(path.size()):
            point = path.inv_pop()
            step = abs(x - point[0][0])
            print(point)

            if step == 0: #y
                step = abs(y - point[0][1])
                h_dir = dir[0][1]
                print('H: ', h_dir)
                for i in range(step):
                    self.solved[x][y + h_dir] = 'O'
                    y += i
            else:
                step = abs(x - point[0][0])
                v_dir = dir[0][0]
                print('V ',  v_dir)
                for i in range(step):
                    self.solved[x + v_dir][y] = 'O'
                    x += i
            dir = point[1]