import mouse as ms
import generator as gn
import pathFinder as pf
import copy

class LogicHandler:
    """Klasa do obsługi logiki programu"""
    def __init__(self):
        self.mouse = ms.Mouse()
        self.__generator = gn.Generator()
        self.__labyrinth = []

        self.__ps_x = 0
        self.__ps_y = 0
        self.__s_x = 0
        self.__s_y = 0

        self.__pe_x = 0
        self.__pe_y = 0
        self.__e_x = 0
        self.__e_y = 0

        self.__pp_x = 0
        self.__pp_y = 0
        self.__points = []

    def generate_mesh(self, size_x, size_y):
        #Tworzy siatkę labiryntu o podanych wartościach i resetuje poprzednie ułożenie
        self.__generator.set_up_generator(size_x, size_y)
        self.__generator.clear()
        self.__labyrinth = self.__generator.get_labyrinth()
        self.__s_x = 0
        self.__s_y = 0
        self.__e_x = 0
        self.__e_y = 0
        self.__points = []

    def generate_labyrinth(self):
        #Generuje labirynt
        self.__pp_x = 0
        self.__pp_y = 0
        self.__generator.clear()

        #Tu zamieniam koordynaty UI na koordynaty generatora
        self.__generator.generate(int(self.__s_x / 2), int(self.__s_y / 2), int(self.__e_x / 2), int(self.__e_y / 2))
        self.__labyrinth = self.__generator.get_labyrinth()

    def generate_solution(self):
        pathFinder = pf.PathFinder()

        #Jeśli nie ma żadnych punktów pośrednich
        if len(self.__points) == 0:
            self.__labyrinth = pathFinder.find(self.__s_x, self.__s_y, self.__e_x, self.__e_y, self.__labyrinth)
        else:
            #Przygotuj pustą siatkę
            clearLab = copy.deepcopy(self.__labyrinth)
            clearLab[self.__s_y][self.__s_x] = ' '
            clearLab[self.__e_y][self.__e_x] = ' '
            for point in self.__points:
                clearLab[point[0]][point[1]] = ' '

            lab_final = copy.deepcopy(self.__labyrinth)

            #Po kolei dodawaj Start i End, a na koniec łącz wszystko w rozwiązanie finalne
            lab_tmp = copy.deepcopy(clearLab)
            lab_tmp[self.__s_y][self.__s_x] = 'S'
            lab_tmp[self.__points[0][0]][self.__points[0][1]] = 'E'
            lab_tmp = pathFinder.find(self.__s_x, self.__s_y, self.__points[0][1], self.__points[0][0], lab_tmp)

            lab_tmp[self.__points[0][0]][self.__points[0][1]] = 'x'
            lab_final = pathFinder.merge_labyrinths_paths(lab_final, lab_tmp)

            for i in range(len(self.__points) - 2):
                lab_tmp = copy.deepcopy(clearLab)
                lab_tmp[self.__points[i][0]][self.__points[i][1]] = 'S'
                lab_tmp[self.__points[i + 1][0]][self.__points[1 + 1][1]] = 'E'
                lab_tmp = pathFinder.find(self.__points[i][1], self.__points[i][0], self.__points[i + 1][1], self.__points[i + 1][0], lab_tmp)
                lab_final = pathFinder.merge_labyrinths_paths(lab_final, lab_tmp)

            last = len(self.__points) - 1
            lab_tmp = copy.deepcopy(clearLab)
            lab_tmp[self.__points[last][0]][self.__points[last][1]] = 'S'
            lab_tmp[self.__e_y][self.__e_x] = 'E'
            lab_tmp = pathFinder.find(self.__points[last][1], self.__points[last][0], self.__e_x, self.__e_y, lab_tmp)

            lab_final = pathFinder.merge_labyrinths_paths(lab_final, lab_tmp)

            #Dodaj końcowe punkty pośrednie
            for point in self.__points:
                lab_final[point[0]][point[1]] = '@'

            self.__labyrinth = copy.deepcopy(lab_final)


    def get_labyrinth(self):
        return self.__labyrinth

    def check_if_ready_to_generate(self):
        #Sprawdza, czy można generować labirynt
        if self.__s_x != 0 and self.__s_y != 0 and self.__e_x != 0 and self.__e_y != 0:
            if self.__s_x != self.__e_x or self.__s_y != self.__e_y:
                return True
        return False

    def check_collisions(self, tile_info):
        #Sprawdza kolizję kwadracika z myszką
        m_x, m_y = self.mouse.get_mouse_position()
        for t_i in tile_info:
            if t_i.check_if_point_is_in(m_x, m_y):
                return t_i.get_grid_position()
        return 0, 0

    def start_picker(self, s_x, s_y):
        #Wybiera punkt startowy
        if self.__s_x != 0 and self.__s_y != 0:
            self.__labyrinth[self.__s_y][self.__s_x] = ' '
            self.__s_x = 0
            self.__s_y = 0

        if self.__ps_x != 0 and self.__ps_y != 0 and self.__labyrinth[self.__ps_y][self.__ps_x] not in ('E', 'S'):
            self.__labyrinth[self.__ps_y][self.__ps_x] = ' '

        if s_x != 0 and s_y != 0:
            if self.mouse.get_mouse_state():
                if s_x != self.__e_x or s_y != self.__e_y:
                    self.__labyrinth[s_y][s_x] = 'S'
                    self.__s_x = s_x
                    self.__s_y = s_y
                    return True

            if self.__labyrinth[s_y][s_x] not in ('E', 'S'):
                self.__labyrinth[s_y][s_x] = '*'
                self.__ps_x = s_x
                self.__ps_y = s_y
        return False

    def end_picker(self, e_x, e_y):
        #Wybiera punkt końcowy
        if self.__e_x != 0 and self.__e_y != 0:
            self.__labyrinth[self.__e_y][self.__e_x] = ' '
            self.__e_x = 0
            self.__e_y = 0

        if self.__pe_x != 0 and self.__pe_y != 0 and self.__labyrinth[self.__pe_y][self.__pe_x] not in ('E', 'S'):
            self.__labyrinth[self.__pe_y][self.__pe_x] = ' '

        if e_x != 0 and e_y != 0:
            if self.mouse.get_mouse_state():
                if e_x != self.__s_x or e_y != self.__s_y:
                    self.__labyrinth[e_y][e_x] = 'E'
                    self.__e_x = e_x
                    self.__e_y = e_y
                    return True

            if self.__labyrinth[e_y][e_x] not in ('E', 'S'):
                self.__labyrinth[e_y][e_x] = '*'
                self.__pe_x = e_x
                self.__pe_y = e_y
        return False

    def point_picker(self, p_x, p_y):
        #Wybiera punkt pośredni
        if self.__pp_x != 0 and self.__pp_y != 0 and self.__labyrinth[self.__pp_y][self.__pp_x] != '%':
            self.__labyrinth[self.__pp_y][self.__pp_x] = ' '

        if p_x != 0 and p_y != 0:
            if self.mouse.get_mouse_state() and self.__labyrinth[p_y][p_x] not in ('E', 'S'):
                i = 0
                poped = False
                for point in self.__points:
                    if point[1] == p_x and point[0] == p_y:
                        self.__points.pop(i)
                        self.__labyrinth[p_y][p_x] = ' '
                        poped = True
                    i += 1

                if not poped:
                    self.__labyrinth[p_y][p_x] = '%'
                    self.__points.append([p_y, p_x])
                self.mouse.reset_state()
                return True

            if self.__labyrinth[p_y][p_x] not in ('E', 'S', '%'):
                self.__labyrinth[p_y][p_x] = '*'
                self.__pp_x = p_x
                self.__pp_y = p_y

        return False

    def get_points(self):
        return self.__points

    def reset_points(self):
        self.__points = []