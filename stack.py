class Stack:
    """Klasa stosu używana do tworzenia labiryntu"""
    def __init__(self):
        self.__st = []

    def push(self, val_1, val_2):
        self.__st.append((val_1, val_2))

    def pop(self):
        if len(self.__st) != 0:
            return self.__st.pop()
        else:
            return [-1]

    def clear(self):
        self.__st = []

    def size(self):
        return len(self.__st)

    def __str__(self):
        str = ""
        for i in self.__st:
            str += "({0} , {1}), ".format(i[0], i[1])
        str += "\n"
        return str
