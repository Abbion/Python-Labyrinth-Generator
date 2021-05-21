import tkinter as tk


class GuiHandler:
    def __init__(self, gfxGuis):
        self.gfx_handle = gfxGuis
        self.rowEntry = gfxGuis.rowEntry
        self.rowEntry.insert(tk.END, "10")

        self.columnEntry = gfxGuis.columnEntry
        self.columnEntry.insert(tk.END, "10")

        self.mesh_render_button = gfxGuis.mesh_render_button
        self.mesh_render_button.configure(command =self.handle_generate_mesh)

        self.start_picker_button_1 = gfxGuis.startButton
        self.start_picker_button_1.configure(command =self.handle_picker_1)

        self.start_picker_button_2 = gfxGuis.endButton
        self.start_picker_button_2.configure(command =self.handle_picker_2)

        self.generate_button = gfxGuis.generateButton
        self.generate_button.configure(command=self.handle_generate)

        self.solve_button = gfxGuis.solve_button
        self.solve_button.configure(command=self.handle_solve)

        self.point_button = gfxGuis.point_button
        self.point_button.configure(command=self.handle_point)

        self.rowValue = 10
        self.columnValue = 10

        self.updateWindow = False
        self.pick_mode_1 = False
        self.pick_mode_2 = False
        self.pick_mode_3 = False
        self.mouse_x = 0
        self.mouse_y = 0

        self.point_picked = False

    def bind_motion_for_root(self, root):
        root.bind('<Motion>', self.mouse_motion)
        root.bind('<Button-1>', self.mouse_click)

    def mouse_motion(self, event):
        if self.check_if_in_pick_mode():
            self.mouse_x = event.x
            self.mouse_y = event.y

    def get_mouse_pos(self):
        return self.mouse_x, self.mouse_y

    def mouse_click(self, event):
        if self.pick_mode_1:
            self.gfx_handle.ss_x = event.x
            self.gfx_handle.ss_y = event.y
            self.mouse_x = 0
            self.mouse_y = 0
            self.pick_mode_1 = False
            self.gfx_handle.renderReady = True
        elif self.pick_mode_2:
            self.gfx_handle.se_x = event.x
            self.gfx_handle.se_y = event.y
            self.mouse_x = 0
            self.mouse_y = 0
            self.pick_mode_2 = False
            self.gfx_handle.renderReady = True
        elif self.pick_mode_3:
            self.point_picked = True
            self.pick_mode_3 = False
            self.updateWindow = True


    def get_entires_values(self):
        return (self.rowValue, self.columnValue)

    def handle_generate_mesh(self):
        if self.validate_entries():
            self.rowValue = int(self.rowEntry.get())
            self.columnValue = int(self.columnEntry.get())
            self.gfx_handle.generator.set_up_generator(self.rowValue, self.columnValue)
            self.gfx_handle.generator.clear()
            self.gfx_handle.labyrinth = self.gfx_handle.generator.get_labyrinth()
            self.start_picker_button_1.configure(state=tk.NORMAL)
            self.start_picker_button_2.configure(state=tk.NORMAL)
            self.solve_button.configure(state=tk.DISABLED)
            self.point_button.configure(state=tk.DISABLED)
            self.gfx_handle.gs_x = -1
            self.gfx_handle.gs_y = -1
            self.gfx_handle.ge_x = -1
            self.gfx_handle.ge_y = -1

            self.updateWindow = True

    def handle_picker_1(self):
        self.pick_mode_1 = True

    def handle_picker_2(self):
        self.pick_mode_2 = True

    def handle_solve(self):
        self.gfx_handle.labyrinth = []

        if len(self.gfx_handle.points) == 0:
            self.gfx_handle.labyrinth = self.gfx_handle.path_finder.find(self.gfx_handle.gs_x * 2 + 1, self.gfx_handle.gs_y * 2 + 1,
                                        self.gfx_handle.ge_x * 2 + 1, self.gfx_handle.ge_y * 2 + 1,
                                         self.gfx_handle.generator.get_labyrinth())
        else:
            p1_x = self.gfx_handle.gs_x * 2 + 1
            p1_y = self.gfx_handle.gs_y * 2 + 1
            labs = []

            for point in self.gfx_handle.points:
                p2_x = point[0] + 1
                p2_y = point[1] + 1

                labs.append(self.gfx_handle.path_finder.find(p1_x, p1_y, p2_x, p2_y, self.gfx_handle.generator.get_labyrinth()))

                p1_x = p2_x
                p1_y = p2_y

            p2_x = self.gfx_handle.ge_x * 2 + 1
            p2_y = self.gfx_handle.ge_y * 2 + 1
            labs.append(self.gfx_handle.path_finder.find(p1_x, p1_y, p2_x, p2_y, self.gfx_handle.generator.get_labyrinth()))

            self.gfx_handle.labyrinth = self.gfx_handle.generator.get_labyrinth()

            for l in labs:
                for y in range(len(l)):
                    for x in range(len(l[0])):
                        if l[y][x] == 'o':
                            self.gfx_handle.labyrinth[y][x] = 'o'

        self.solve_button.configure(state=tk.DISABLED)
        self.point_button.configure(state=tk.DISABLED)
        self.updateWindow = True

    def handle_point(self):
        self.pick_mode_3 = True

    def handle_generate(self):
        self.gfx_handle.generator.clear()
        self.gfx_handle.generator.generate(self.gfx_handle.gs_x, self.gfx_handle.gs_y, self.gfx_handle.ge_x, self.gfx_handle.ge_y)
        self.gfx_handle.labyrinth = self.gfx_handle.generator.get_labyrinth()
        self.updateWindow = True

        self.start_picker_button_1.configure(state=tk.DISABLED)
        self.start_picker_button_2.configure(state=tk.DISABLED)
        self.solve_button.configure(state=tk.NORMAL)
        self.point_button.configure(state=tk.NORMAL)
        self.gfx_handle.points = []

    def check_if_in_pick_mode(self):
        return self.pick_mode_1 or self.pick_mode_2 or self.pick_mode_3

    def get_picker_id(self):
        if self.pick_mode_1:
            return 1
        elif self.pick_mode_2:
            return 2
        elif self.pick_mode_3:
            return 3
        else:
            return 0

    def validate_entries(self):
        def validate_1(entry):
            entry_str = entry.get()
            entry_str = entry_str.strip()
            if entry_str.isdecimal():
                val = int(entry_str)
                if val < 3 or val > 30:
                    entry.configure(bg='red')
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, entry_str)
                    return False

                entry.configure(bg='white')
                entry.delete(0, tk.END)
                entry.insert(tk.END, entry_str)
                return True

            else:
                entry.configure(bg='red')
                return False

        def validate_2(entry):
            EntryStr = entry.get()
            EntryStr = EntryStr.strip()
            spl = EntryStr.split(",")

            if(len(spl) != 2):
                entry.configure(bg='red')
                entry.delete(0, tk.END)
                entry.insert(tk.END, EntryStr)
                return False

            valComp = self.get_entires_values()

            for i in range(2):
                numStr = spl[i].strip()

                if numStr.isdecimal():
                    val = int(numStr)
                    if val < 1 or val > round(valComp[i] / 2):
                        entry.configure(bg='red')
                        entry.delete(0, tk.END)
                        entry.insert(tk.END, EntryStr)
                        return False
                else:
                    entry.configure(bg='red')
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, EntryStr)
                    return False

            entry.configure(bg='white')
            entry.delete(0, tk.END)
            entry.insert(tk.END, EntryStr)
            return True


        v_1_b = validate_1(self.rowEntry)
        v_2_b = validate_1(self.columnEntry)
        if v_1_b and v_2_b:
            return True
        return False

