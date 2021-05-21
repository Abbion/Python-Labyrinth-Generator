import window as win
import graphics as gfx
import test

class App:
    def __init__(self):
        self.window = win.Window()
        self.graphics = gfx.Graphics()
        self.graphics.guiHandler.bind_motion_for_root(self.window.get_window_root())

    def update(self):
        if self.window.check_window_resize():
            self.graphics.rescale(self.window.get_size())

        if self.graphics.is_render_ready():
            self.graphics.clear()
            self.graphics.draw()
            self.graphics.display()

        self.window.set_update(self.update, 60)

    def startLoop(self):
        self.window.set_update(self.update, 60)
        self.window.loop()

def main():
    app = App()
    app.startLoop()
    #test.test()



if __name__ == '__main__':
    main()
