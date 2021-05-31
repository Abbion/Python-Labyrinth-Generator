class Tile:
    """Klasa przedstawiająca pozycję bloczka"""

    def __init__(self, s_x, s_y, e_x, e_y, g_x, g_y):
        self.__s_x = s_x
        self.__s_y = s_y
        self.__e_x = e_x
        self.__e_y = e_y
        self.__g_x = g_x
        self.__g_y = g_y

    def check_if_point_is_in(self, x, y):
        #Sprawdzenie, czy punkt jest w bloczku
        if x >= self.__s_x and x <= self.__e_x and y >= self.__s_y and y <= self.__e_y:
            return True
        return False

    def get_grid_position(self):
        #Pozycja na siatce
        return self.__g_x, self.__g_y


