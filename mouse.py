
class Mouse:
    """ Klasa obsługująca myszkę"""
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__lbDown = False

    def bind_mouse(self, window_root):
        #Przypisuje eventy myszki do funkcji
        window_root.bind('<Motion>', self.__mouse_motion)
        window_root.bind('<Button-1>', self.__mouse_click)
        window_root.bind('<ButtonRelease-1>', self.__mouse_release)

    def __mouse_motion(self, event):
        self.__x = event.x
        self.__y = event.y

    def __mouse_click(self, event):
        self.__lbDown = True

    def __mouse_release(self, event):
        self.__lbDown = False

    def get_mouse_position(self):
        return self.__x, self.__y

    def get_mouse_state(self):
        return self.__lbDown

    def reset_state(self):
        self.__lbDown = False
