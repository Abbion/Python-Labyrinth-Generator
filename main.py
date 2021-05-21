import window as win
import graphics as gfx
import test

class App:
    def __init__(self):
        self.window = win.Window()
        self.graphics = gfx.Graphics()
        self.graphics.guiHandler.bind_motion_for_root(self.window.get_window_root())

    def update(self):
        if self.window.checkWindowResize():
            self.graphics.rescale(self.window.getSize())

        if self.graphics.isRenderReady():
            self.graphics.clear()
            self.graphics.draw()
            self.graphics.display()

        self.window.setUpdate(self.update, 60)

    def startLoop(self):
        self.window.setUpdate(self.update, 60)
        self.window.loop()

def main():
    app = App()
    app.startLoop()
    #test.test()



if __name__ == '__main__':
    main()
