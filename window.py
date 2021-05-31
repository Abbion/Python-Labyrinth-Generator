import  tkinter as tk

class Window:
    """Klasa tworząca okno"""
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("Generator labiryntów")
        self.__initialSize = (1000, 800)
        self.__size = (1000, 800)
        self.__window.geometry("1000x800")
        self.__window.minsize(600, 500)

    def set_update(self, updateFunction, time = 1):
        self.__window.after(time, updateFunction)

    def loop(self):
        self.__window.mainloop()

    def get_size(self):
        return (self.__window.winfo_width(), self.__window.winfo_height())

    def check_window_resize(self):
        size = self.get_size()
        if size[0] != self.__size[0] or size[1] != self.__size[1]:
            self.__size = size
            return True
        return False

    def get_window_root(self):
        return self.__window