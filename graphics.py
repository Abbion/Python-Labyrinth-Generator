import tkinter as tk
import guiHandler as gh
import colors
import tile as tl

class Graphics(tk.Frame):
    """Klasa do obsługi grafiki"""
    def __init__(self):
        super().__init__()

        self.__GUIyStart = 10
        self.__GUIStep = 25
        self.__padding = 20
        self.__gui_padding = 125
        self.__windowSize = (1000, 800)
        self.__renderReady = True

        self.__tile_info = []

        self.__set_up_GUI()
        self.__guiHandler = gh.GuiHandler(self)

        self.__labyrinth_set_up()

    def get_gui_handler(self):
        return self.__guiHandler

    def __set_up_GUI(self):
        #Ustawienie GUI
        nextYpos = self.__GUIyStart
        self.pack(fill=tk.BOTH, expand=1)
        self.GUIcanvas = tk.Canvas(self, bd = 0)

        #Nie ustawiam tych pól na prywatne, gdyż guiHandler musi mieć do nich dostęp
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
        self.mesh_render_button = tk.Button(text="Generuj\n siatke")
        nextYpos += self.__GUIStep
        self.mesh_render_button.place(x=10, y=nextYpos, height=40, width=80)

        self.startLabel = tk.Label(text="Początek labiryntu")
        nextYpos += 2.5 * self.__GUIStep
        self.startLabel.place(x=10, y=nextYpos)
        self.startButton = tk.Button(text="Wybierz")
        nextYpos += 1.2 * self.__GUIStep
        self.startButton.place(x=10, y=nextYpos, height=20, width=80)

        self.endLabel = tk.Label(text="Koniec labiryntu")
        nextYpos += self.__GUIStep
        self.endLabel.place(x=10, y=nextYpos)
        self.endButton = tk.Button(text="Wybierz")
        nextYpos += 1.2 * self.__GUIStep
        self.endButton.place(x=10, y=nextYpos, height=20, width=80)

        self.generateButton = tk.Button(text="Generuj\nlabirynt", state=tk.DISABLED)
        nextYpos += 1.2 * self.__GUIStep
        self.generateButton.place(x=10, y=nextYpos, height=40, width=80)

        self.point_button = tk.Button(text="Dodaj\npunkt", state=tk.DISABLED)
        nextYpos += 2.4 * self.__GUIStep
        self.point_button.place(x=10, y=nextYpos, height=40, width=80)

        self.solve_button = tk.Button(text="Rozwiąż\nlabirynt", state=tk.DISABLED)
        nextYpos += 2.4 * self.__GUIStep
        self.solve_button.place(x=10, y=nextYpos, height=40, width=80)

    def __labyrinth_set_up(self):
        #Ustawia płutno pod labirynt
        self.LabCanvas = tk.Canvas(self, bd = 0)

    def get_tile_info(self):
        return self.__tile_info

    def rescale(self, size):
        #Ustawia skalę dla UI
        self.__windowSize = size
        self.__renderReady = True

    def clear(self):
        #Czyści ekrany
        self.LabCanvas.delete("all")
        self.GUIcanvas.delete("all")

    def draw(self, lab_layout):
        #Linia oddzielająca UI
        self.GUIcanvas.create_line(120, 0, 120, self.__windowSize[1], fill=colors.Gui_Line)

        #Labirynt
        start = (self.__padding, + self.__padding)
        end = (self.__windowSize[0] - self.__padding - self.__gui_padding, self.__windowSize[1] - self.__padding)
        canvas_size = (self.__windowSize[0] - 2 * self.__padding - self.__gui_padding, self.__windowSize[1] - 2 * self.__padding)

        self.LabCanvas.create_rectangle(start[0], start[1], end[0], end[1], fill=colors.bg)

        #Sprawdzanie, czy da się narysować labirynt
        if len(lab_layout) > 1 and len(lab_layout[0]) > 1:
            self.__tile_info = []
            height_in_blocks = len(lab_layout)
            width_in_blocks = len(lab_layout[0])

            dx = canvas_size[0] / width_in_blocks
            dy = canvas_size[1] / height_in_blocks

            x_pos = start[0]
            y_pos = start[1]
            g_x = 0
            g_y = 0

            #Rozłożenie labiryntu i pokolorowanie odpowiednich fragmentów
            for row in lab_layout:
                for tile in row:
                    if tile != '█':
                        if tile == ' ':
                            self.LabCanvas.create_rectangle(x_pos, y_pos, x_pos + dx, y_pos + dy,
                                                            fill=colors.fr, outline="")
                        elif tile == '*':
                            self.LabCanvas.create_rectangle(x_pos, y_pos, x_pos + dx, y_pos + dy,
                                                            fill=colors.p_pick, outline="")

                        elif tile == 'S':
                            self.LabCanvas.create_rectangle(x_pos, y_pos, x_pos + dx, y_pos + dy,
                                                            fill=colors.s_pick, outline="")

                        elif tile == 'E':
                            self.LabCanvas.create_rectangle(x_pos, y_pos, x_pos + dx, y_pos + dy,
                                                            fill=colors.e_pick, outline="")

                        elif tile == '%':
                            self.LabCanvas.create_rectangle(x_pos, y_pos, x_pos + dx, y_pos + dy,
                                                            fill=colors.p_pick, outline="")
                        elif tile == 'o':
                            self.LabCanvas.create_rectangle(x_pos, y_pos, x_pos + dx, y_pos + dy,
                                                            fill=colors.correct_path, outline="")
                        elif tile == 'x':
                            self.LabCanvas.create_rectangle(x_pos, y_pos, x_pos + dx, y_pos + dy,
                                                            fill=colors.wrong_path, outline="")
                        elif tile == '@':
                            self.LabCanvas.create_rectangle(x_pos, y_pos, x_pos + dx, y_pos + dy,
                                                            fill=colors.point, outline="")

                        self.__tile_info.append(tl.Tile(x_pos, y_pos, x_pos + dx, y_pos + dy, g_x, g_y))

                    g_x += 1
                    x_pos += dx

                g_x = 0
                x_pos = start[0]
                g_y += 1
                y_pos += dy

    def display(self):
        self.GUIcanvas.place(x = 0, y = 0, width = 125, height = self.__windowSize[1])
        self.LabCanvas.place(x=125, y=0, width=self.__windowSize[0] - 125, height=self.__windowSize[1])
        self.__renderReady = False

    def is_render_ready(self):
        #Zwraca true, jeśli trzeba wyrenderować UI
        return self.__renderReady