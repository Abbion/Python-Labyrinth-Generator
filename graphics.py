import tkinter as tk
import guiHandler as gh
import generator as gn
import pathFinder as pf
import colors
import tile as tl

class Graphics(tk.Frame):
    def __init__(self):
        super().__init__()

        self.__GUIyStart = 10
        self.__GUIStep = 25
        self.__padding = 20
        self.__gui_padding = 125
        self.__windowSize = (1000, 800)
        self.renderReady = True

        self.__tile_info = []

        self.gs_x = -1
        self.gs_y = -1

        self.ge_x = -2
        self.ge_y = -2

        self.gp_x = -1
        self.gp_y = -1

        self.__set_up_GUI()
        self.__guiHandler = gh.GuiHandler(self)

        self.__labirynth_set_up()

        self.generator = gn.Generator()
        s_x, s_y = self.__guiHandler.get_labyrinth_size()
        self.generator.set_up_generator(s_x, s_y)
        self.generator.clear()

        self.path_finder = pf.PathFinder()

        self.labyrinth = self.generator.get_labyrinth()
        self.points = []

    def get_gui_handler(self):
        return self.__guiHandler

    def __set_up_GUI(self):
        #Ustawienie GUI
        nextYpos = self.__GUIyStart
        self.pack(fill=tk.BOTH, expand=1)
        self.GUIcanvas = tk.Canvas(self, bd = 0)

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



    def __labirynth_set_up(self):
        self.LabCanvas = tk.Canvas(self, bd = 0)

    def get_tile_info(self):
        return self.__tile_info

    def rescale(self, size):
        self.__windowSize = size
        self.renderReady = True

    def clear(self):
        self.LabCanvas.delete("all")
        self.GUIcanvas.delete("all")

    def draw(self, lab_layout):
        self.GUIcanvas.create_line(120, 0, 120, self.__windowSize[1], fill=colors.Gui_Line)

        start = (self.__padding, + self.__padding)
        end = (self.__windowSize[0] - self.__padding - self.__gui_padding, self.__windowSize[1] - self.__padding)
        canvas_size = (self.__windowSize[0] - 2 * self.__padding - self.__gui_padding, self.__windowSize[1] - 2 * self.__padding)

        self.LabCanvas.create_rectangle(start[0], start[1], end[0], end[1], fill=colors.bg)

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


        """
        dx = canvas_size[0] / (len(self.labyrinth[0]))
        dy = canvas_size[1] / (len(self.labyrinth))

        n_start = [start[0] + self.__gui_padding, start[1]]

        
        mp_x, mp_y = self.guiHandler.get_mouse_pos()
        g_x = 0
        g_y = 0

        for row in self.labyrinth:
            for block in row:
                if block != '█':
                    if mp_x > n_start[0] and mp_x < n_start[0] + dx and mp_y > n_start[1] and mp_y < n_start[1] + dy:
                        if self.guiHandler.get_picker_id() == 1:
                            self.gs_x = int(g_x)
                            self.gs_y = int(g_y)
                        if self.guiHandler.get_picker_id() == 2:
                            self.ge_x = int(g_x)
                            self.ge_y = int(g_y)
                        if self.guiHandler.get_picker_id() == 3:
                            self.gp_x = int((mp_x - self.__padding) / dx - 1)
                            self.gp_y = int((mp_y - self.__padding) / dy - 1)

                    if block == 'x':
                        self.LabCanvas.create_rectangle(n_start[0], n_start[1], n_start[0] + dx, n_start[1] + dy,
                                                        fill=colors.wrong_path, outline="")
                    elif block == 'o':
                        self.LabCanvas.create_rectangle(n_start[0], n_start[1], n_start[0] + dx, n_start[1] + dy,
                                                        fill=colors.correct_path, outline="")
                    else:
                        self.LabCanvas.create_rectangle(n_start[0], n_start[1], n_start[0] + dx, n_start[1] + dy, fill=colors.fr,  outline="")
                    g_x += 1
                n_start[0] += dx
            if row[1] != '█':
                g_y += 1

            n_start[1] += dy
            n_start[0] = self.__padding
            g_x = 0

        labyrinth_set_correctly = [False, False, True]
        if self.gs_x >= 0 and self.gs_y >= 0:
            self.LabCanvas.create_rectangle(start[0] + dx * (self.gs_x * 2 + 1), start[1] + dy * (self.gs_y * 2 + 1),
                                            start[0] + dx * (self.gs_x * 2 + 2), start[1] + dy * (self.gs_y * 2 + 2),
                                            fill=colors.s_pick, outline="")
            labyrinth_set_correctly[0] = True

        if self.ge_x >= 0 and self.ge_y >= 0:
            self.LabCanvas.create_rectangle(start[0] + dx * (self.ge_x * 2 + 1), start[1] + dy * (self.ge_y * 2 + 1),
                                            start[0] + dx * (self.ge_x * 2 + 2), start[1] + dy * (self.ge_y * 2 + 2),
                                            fill=colors.e_pick, outline="")
            labyrinth_set_correctly[1] = True

        if self.gp_x >= 0 and self.gp_y >= 0 and self.guiHandler.get_picker_id() == 3:
            self.LabCanvas.create_rectangle(start[0] + dx * (self.gp_x + 1), start[1] + dy * (self.gp_y + 1),
                                            start[0] + dx * (self.gp_x + 2), start[1] + dy * (self.gp_y + 2),
                                            fill=colors.p_pick, outline="")


        if self.gs_x == self.ge_x and self.gs_y == self.ge_y:
            labyrinth_set_correctly[2] = False

        if labyrinth_set_correctly[0] and labyrinth_set_correctly[1] and labyrinth_set_correctly[2] and self.guiHandler.get_picker_id() == 0:
            self.generateButton.configure(state=tk.NORMAL)
        else:
            self.generateButton.configure(state=tk.DISABLED)


        if self.guiHandler.point_picked:
            self.points.append((self.gp_x, self.gp_y))
            last = self.points.pop()
            for i in range(len(self.points)):
                if last[0] == self.points[i][0] and last[1] == self.points[i][1]:
                    print(last)
                    self.LabCanvas.create_rectangle(start[0] + dx * (last[0] + 1), start[1] + dy * (last[1] + 1),
                                                    start[0] + dx * (last[0] + 2), start[1] + dy * (last[1] + 2),
                                                    fill=colors.fr, outline="")
                    del self.points[i]
                    break
            else:
                self.points.append(last)

        self.guiHandler.point_picked = False

        for point in self.points:
            self.LabCanvas.create_rectangle(start[0] + dx * (point[0] + 1), start[1] + dy * (point[1] + 1),
                                            start[0] + dx * (point[0] + 2), start[1] + dy * (point[1] + 2),
                                            fill=colors.point, outline="")
    """
    def display(self):
        self.GUIcanvas.place(x = 0, y = 0, width = 125, height = self.__windowSize[1])
        self.LabCanvas.place(x=125, y=0, width=self.__windowSize[0] - 125, height=self.__windowSize[1])
        self.renderReady = False

    def is_render_ready(self):
        return self.renderReady