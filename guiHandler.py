import tkinter as tk
import myException
import myException as exc

#Typy Eventów
nullEvent = 0
generateMeshEvent = 1
solveEvent = 2
generateLabyrinthEvent = 3

class GuiHandler:
    """Klasa do obsługi zdarzeń GUI"""
    def __init__(self, gfxGuis):
        #Ustawienie reakcji na elementy GUI
        self.__rowEntry = gfxGuis.rowEntry
        self.__rowEntry.insert(tk.END, "10")

        self.__columnEntry = gfxGuis.columnEntry
        self.__columnEntry.insert(tk.END, "10")

        self.__mesh_render_button = gfxGuis.mesh_render_button
        self.__mesh_render_button.configure(command =self.__handle_generate_mesh)

        self.__start_picker_button_1 = gfxGuis.startButton
        self.__start_picker_button_1.configure(command = self.__handle_picker_1)

        self.__start_picker_button_2 = gfxGuis.endButton
        self.__start_picker_button_2.configure(command =self.__handle_picker_2)

        self.__generate_button = gfxGuis.generateButton
        self.__generate_button.configure(command=self.__handle_generate)

        self.__solve_button = gfxGuis.solve_button
        self.__solve_button.configure(command=self.__handle_solve)

        self.__point_button = gfxGuis.point_button
        self.__point_button.configure(command=self.__handle_picker_3)

        #Wielkość początkowa labiryntu
        self.__rowValue = 10
        self.__columnValue = 10

        self.__pickerMode = 0
        self.__guiEvent = nullEvent

    def get_labyrinth_size(self):
        return self.__rowValue, self.__columnValue

    def get_gui_event(self):
        save_event = self.__guiEvent
        self.__guiEvent = nullEvent
        return save_event

    def __handle_generate_mesh(self):
        #Walidacja wartości i przygotowanie programu do dalszej pracy
        try:
            self.__validate_entries()

            self.__rowValue = int(self.__rowEntry.get())
            self.__columnValue = int(self.__columnEntry.get())
            self.__start_picker_button_1.configure(state=tk.NORMAL)
            self.__start_picker_button_2.configure(state=tk.NORMAL)
            self.__solve_button.configure(state=tk.DISABLED)
            self.__point_button.configure(state=tk.DISABLED)
            self.__guiEvent = generateMeshEvent

        except myException.WrongEntryException as e:
            #Wypisanie błędu
            print(e)
            if e.get_entry_id() == 1:
                self.__rowEntry.configure(bg='red')
            elif e.get_entry_id() == 2:
                self.__columnEntry.configure(bg='red')

    def __handle_solve(self):
        self.__solve_button.configure(state=tk.DISABLED)
        self.__point_button.configure(state=tk.DISABLED)
        self.__guiEvent = solveEvent

    def __handle_generate(self):
        self.__guiEvent = generateLabyrinthEvent

        self.__start_picker_button_1.configure(state=tk.DISABLED)
        self.__start_picker_button_2.configure(state=tk.DISABLED)
        self.__solve_button.configure(state=tk.NORMAL)
        self.__point_button.configure(state=tk.NORMAL)

    def __handle_picker_1(self):
        self.__pickerMode = 1

    def __handle_picker_2(self):
        self.__pickerMode = 2

    def __handle_picker_3(self):
        self.__pickerMode = 3

    def reset_picker(self):
        self.__pickerMode = 0

    def get_picker_mode(self):
        return self.__pickerMode

    def __validate_entries(self):
        def validate_1(entry, entry_id):
            entry_str = entry.get()
            entry_str = entry_str.strip()
            if entry_str.isdecimal():
                val = int(entry_str)
                if val < 3 or val > 30:
                    raise exc.WrongEntryException("wartość poza zakresem", entry_id)

                entry.configure(bg='white')
                entry.delete(0, tk.END)
                entry.insert(tk.END, entry_str)
            else:
                raise exc.WrongEntryException("wartość nie jest liczbą", entry_id)

        validate_1(self.__rowEntry, 1)
        validate_1(self.__columnEntry, 2)

    def set_generate_button(self, setter):
        #Blokuje lub odblokowuje dostęp do generowania
        if setter:
            self.__generate_button.configure(state=tk.NORMAL)
        else:
            self.__generate_button.configure(state=tk.DISABLED)