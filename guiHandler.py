import  tkinter as tk


class GuiHandler:
    def __init__(self, gfxGuis):
        self.rowEntry = gfxGuis.rowEntry
        self.rowEntry.insert(tk.END, "10")

        self.columnEntry = gfxGuis.columnEntry
        self.columnEntry.insert(tk.END, "10")

        self.startEntry = gfxGuis.startEntry
        self.startEntry.insert(tk.END, "1, 1")

        self.endEntry = gfxGuis.endEntry
        self.endEntry.insert(tk.END, "5, 5")

        self.generateButton = gfxGuis.generateButton
        self.generateButton.configure(command =self.handleGeneratePress)

        self.renderReady = gfxGuis.renderReady

        self.rowValue = 10
        self.columnValue = 10

        self.updateWindow = False

    def getEntiresValues(self):
        return (self.rowValue, self.columnValue)

    def handleGeneratePress(self):
        if self.validateEntries():
            self.rowValue = int(self.rowEntry.get())
            self.columnValue = int(self.columnEntry.get())
            self.updateWindow = True

    def validateEntries(self):
        def validate_1(entry):
            EntryStr = entry.get()
            EntryStr = EntryStr.strip()
            if EntryStr.isdecimal():
                val = int(EntryStr)
                if val < 1 or val > 30:
                    entry.configure(bg='red')
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, EntryStr)
                    return False

                entry.configure(bg='white')
                entry.delete(0, tk.END)
                entry.insert(tk.END, EntryStr)
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

            valComp = self.getEntiresValues()

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



        if validate_1(self.rowEntry) and validate_1(self.columnEntry) and validate_2(self.startEntry) and validate_2(self.endEntry):
            return True
        return False

