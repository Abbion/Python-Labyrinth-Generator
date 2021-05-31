import window as win
import graphics as gfx
import guiHandler as gh
import logicHandler as lg

class App:
    def __init__(self):
        self.window = win.Window()
        self.graphics = gfx.Graphics()
        self.guiHandler = self.graphics.get_gui_handler()
        self.logic = lg.LogicHandler()
        self.logic.mouse.bind_mouse(self.window.get_window_root())

    def update(self):
        if self.window.check_window_resize():
            self.graphics.rescale(self.window.get_size())

        updateScreen = False
        event = self.guiHandler.get_gui_event()

        if event == gh.generateMeshEvent:
            s_x, s_y = self.guiHandler.get_labyrinth_size()
            self.logic.generate_mesh(s_x, s_y)
            self.guiHandler.set_generate_button(False)
            updateScreen = True

        elif event == gh.generateLabyrinthEvent:
            self.logic.generate_labyrinth()
            self.logic.reset_points()
            updateScreen = True

        elif event == gh.solveEvent:
            self.logic.generate_solution()
            self.guiHandler.reset_picker()
            updateScreen = True

        if self.guiHandler.get_picker_mode() == 1:
            sp_x, sp_y = self.logic.check_collisions(self.graphics.get_tile_info())
            if self.logic.start_picker(sp_x, sp_y):
                self.guiHandler.reset_picker()

            if self.logic.check_if_ready_to_generate():
                self.guiHandler.set_generate_button(True)
            else:
                self.guiHandler.set_generate_button(False)
            updateScreen = True

        if self.guiHandler.get_picker_mode() == 2:
            ep_x, ep_y = self.logic.check_collisions(self.graphics.get_tile_info())
            if self.logic.end_picker(ep_x, ep_y):
                self.guiHandler.reset_picker()

            if self.logic.check_if_ready_to_generate():
                self.guiHandler.set_generate_button(True)
            else:
                self.guiHandler.set_generate_button(False)

            updateScreen = True

        if self.guiHandler.get_picker_mode() == 3:
            pp_x, pp_y = self.logic.check_collisions(self.graphics.get_tile_info())
            if self.logic.point_picker(pp_x, pp_y):
                self.guiHandler.reset_picker()
            updateScreen = True

        if self.graphics.is_render_ready() or updateScreen:
            self.graphics.clear()
            self.graphics.draw(self.logic.get_labyrinth())
            self.graphics.display()

        self.window.set_update(self.update, 30)

    def startLoop(self):
        self.window.set_update(self.update, 30)
        self.window.loop()

def main():
    app = App()
    app.startLoop()
    #test.test()

if __name__ == '__main__':
    main()
