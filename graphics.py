import array
import  tkinter as tk
import guiHandler as gh
import numpy as np

class Graphics(tk.Frame):
    def __init__(self):
        super().__init__()

        self.__GUIyStart = 10
        self.__GUIStep = 25
        self.__padding = 20
        self.__windowSize = (1000, 800)
        self.renderReady = True

        self.__setUpGUI()
        self.__LabirynthSetUp()


    def __setUpGUI(self):
        nextYpos = self.__GUIyStart
        self.pack(fill=tk.BOTH, expand=1)
        self.GUIcanvas = tk.Canvas(self, bg = "#ffaaaa", bd = 0)

        self.rowLabel = tk.Label(text="Ilość rzędów")
        self.rowLabel.place(x=10, y=nextYpos)
        self.rowEntry = tk.Entry()
        nextYpos += self.__GUIStep
        self.rowEntry.place(x=10, y=nextYpos, width=80)

        self.columnLabel = tk.Label(text="Ilość kolumn")
        nextYpos += self.__GUIStep
        self.columnLabel.place(x=10, y=nextYpos)
        self.columnEntry = tk.Entry()
        nextYpos += self.__GUIStep
        self.columnEntry.place(x=10, y=nextYpos, width=80)

        self.startLabel = tk.Label(text="Początek labiryntu")
        nextYpos += 2 * self.__GUIStep
        self.startLabel.place(x=10, y=nextYpos)
        self.startEntry = tk.Entry()
        nextYpos += self.__GUIStep
        self.startEntry.place(x=10, y=nextYpos, width=80)
        #self.startButton = tk.Button(text="Wybierz")
        #nextYpos += 1.2 * self.__GUIStep
        #self.startButton.place(x=10, y=nextYpos, height=20, width=80)

        self.endLabel = tk.Label(text="Koniec labiryntu")
        nextYpos += self.__GUIStep
        self.endLabel.place(x=10, y=nextYpos)
        self.endEntry = tk.Entry()
        nextYpos += self.__GUIStep
        self.endEntry.place(x=10, y=nextYpos, width=80)
        #self.endButton = tk.Button(text="Wybierz")
        #nextYpos += 1.2 * self.__GUIStep
        #self.endButton.place(x=10, y=nextYpos, height=20, width=80)

        self.generateButton = tk.Button(text="Generuj")
        nextYpos += 2.5 * self.__GUIStep
        self.generateButton.place(x=10, y=nextYpos, height=20, width=80)

        self.guiHandler = gh.GuiHandler(self)


    def __LabirynthSetUp(self):
        self.LabCanvas = tk.Canvas(self, bg = "#aaffff", bd = 0)


    def rescale(self, size):
        self.__windowSize = size
        self.renderReady = True


    def clear(self):
        self.LabCanvas.delete("all")
        self.GUIcanvas.delete("all")

    def draw(self):
        self.GUIcanvas.create_line(120, 0, 120, self.__windowSize[1], fill="#A0A0A0")

        minSquare = self.__windowSize[0] - 125 - self.__padding
        if minSquare >  self.__windowSize[1] - self.__padding:
            minSquare = self.__windowSize[1] - self.__padding

        start = ((self.__windowSize[0] - 125) / 2 - minSquare / 2, self.__windowSize[1] / 2 - minSquare / 2)
        end = (start[0] + minSquare, start[1] + minSquare)
        self.LabCanvas.create_rectangle(start[0], start[1], end[0], end[1], fill="#000000")

        labSize = self.guiHandler.getEntiresValues()

        dx = minSquare / (labSize[0] + 2)
        dy = minSquare / (labSize[1] + 2)

        if labSize[0] % 2 == 0:
            dx = minSquare / (labSize[0] + 1)
        if labSize[1] % 2 == 0:
            dy = minSquare / (labSize[1] + 1)

        nStart = np.array(start)

        for i in range(labSize[1]):
            nStart[1] += dy
            for j in range(labSize[0]):
                nStart[0] += dx
                if j % 2 == 1 or i % 2 == 1:
                    self.LabCanvas.create_rectangle(nStart[0], nStart[1], nStart[0] + dx, nStart[1] + dy, fill="#bbbb00")
                else:
                    self.LabCanvas.create_rectangle(nStart[0], nStart[1], nStart[0] + dx, nStart[1] + dy, fill="#ff0000")

            nStart[0] = start[0]


    def display(self):
        self.GUIcanvas.place(x = 0, y = 0, width = 125, height = self.__windowSize[1])
        self.LabCanvas.place(x=125, y=0, width=self.__windowSize[0] - 125, height=self.__windowSize[1])
        self.renderReady = False

    def isRenderReady(self):
        return self.renderReady
