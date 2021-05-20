import window as win
import graphics as gfx
import  generator as gen
import  pathFinder as pf

class App:
    def __init__(self):
        self.window = win.Window()
        self.graphics = gfx.Graphics()

    def update(self):
        if self.window.checkWindowResize():
            self.graphics.rescale(self.window.getSize())

        if self.graphics.isRenderReady() or self.graphics.guiHandler.updateWindow:
            self.graphics.clear()
            self.graphics.draw()
            self.graphics.display()

        self.window.setUpdate(self.update, 30)

    def startLoop(self):
        self.window.setUpdate(self.update, 30)
        self.window.loop()

def main():
    #app = App()
    #app.startLoop()

    g = gen.Generator()
    p = pf.PathFinder()

    g.set_up_generator(30, 20)
    g.clear()

    g.generate(0, 0, 14, 9)

    a = g.get_labyrinth()

    for i in range(len(g.get_labyrinth())):
        for j in g.get_labyrinth()[i]:
            print(j, end=' ')
        print()


    AM = p.find(1, 1, 29, 19, a)
    print()

    for i in range(len(AM)):
        for j in AM[i]:
            print(j, end=' ')
        print()

if __name__ == '__main__':
    main()
