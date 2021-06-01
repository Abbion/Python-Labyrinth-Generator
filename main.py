import mouse
import window as win
import graphics as gfx
import guiHandler as gh
import logicHandler as lg

class App:
    """Klasa aplikajci"""
    def __init__(self):
        self.__window = win.Window()
        self.__graphics = gfx.Graphics()
        self.__guiHandler = self.__graphics.get_gui_handler()
        self.__logic = lg.LogicHandler()
        self.__logic.mouse.bind_mouse(self.__window.get_window_root())

    def update(self):
        if self.__window.check_window_resize():
            self.__graphics.rescale(self.__window.get_size())

        #Zmienna mówiąca, czy trzeba zaktualizować erkan
        updateScreen = False
        #Pobieranie eventu
        event = self.__guiHandler.get_gui_event()

        #Obsługa eventów
        if event == gh.generateMeshEvent:
            s_x, s_y = self.__guiHandler.get_labyrinth_size()
            self.__logic.generate_mesh(s_x, s_y)
            self.__guiHandler.set_generate_button(False)
            updateScreen = True

        elif event == gh.generateLabyrinthEvent:
            self.__logic.generate_labyrinth()
            self.__logic.reset_points()
            updateScreen = True

        elif event == gh.solveEvent:
            self.__logic.generate_solution()
            self.__guiHandler.reset_picker()
            updateScreen = True

        #Obsługa wybierania
        if self.__guiHandler.get_picker_mode() == 1:
            sp_x, sp_y = self.__logic.check_collisions(self.__graphics.get_tile_info())
            if self.__logic.start_picker(sp_x, sp_y):
                self.__guiHandler.reset_picker()

            if self.__logic.check_if_ready_to_generate():
                self.__guiHandler.set_generate_button(True)
            else:
                self.__guiHandler.set_generate_button(False)
            updateScreen = True

        if self.__guiHandler.get_picker_mode() == 2:
            ep_x, ep_y = self.__logic.check_collisions(self.__graphics.get_tile_info())
            if self.__logic.end_picker(ep_x, ep_y):
                self.__guiHandler.reset_picker()

            if self.__logic.check_if_ready_to_generate():
                self.__guiHandler.set_generate_button(True)
            else:
                self.__guiHandler.set_generate_button(False)

            updateScreen = True

        if self.__guiHandler.get_picker_mode() == 3:
            pp_x, pp_y = self.__logic.check_collisions(self.__graphics.get_tile_info())
            if self.__logic.point_picker(pp_x, pp_y):
                self.__guiHandler.reset_picker()
            updateScreen = True

        #Rysowanie
        if self.__graphics.is_render_ready() or updateScreen:
            self.__graphics.clear()
            self.__graphics.draw(self.__logic.get_labyrinth())
            self.__graphics.display()

        self.__window.set_update(self.update, 30)

    def startLoop(self):
        self.__window.set_update(self.update, 30)
        self.__window.loop()

def main():
    app = App()
    app.startLoop()
    #test.test()

if __name__ == '__main__':
    main()
