import  tkinter as tk

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Generator labiryntów")
        self.initialSize = (1000, 800)
        self.size = (1000, 800)
        self.window.geometry("1000x800")
        self.window.minsize(600, 500)

    def setUpdate(self, updateFunction, time = 1):
        self.window.after(time, updateFunction)

    def loop(self):
        self.window.mainloop()

    def getSize(self):
        return (self.window.winfo_width(), self.window.winfo_height())

    def checkWindowResize(self):
        size = self.getSize()
        if size[0] != self.size[0] or size[1] != self.size[1]:
            self.size = size
            return True
        return False

    def getResizeRatio(self):
        return (self.size / self.initialSize, self.size / self.initialSize)

    def get_window_root(self):
        return self.window