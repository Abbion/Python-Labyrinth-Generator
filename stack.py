class Stack:
    def __init__(self):
        self.st = []

    def push(self, val_1, val_2):
        self.st.append((val_1, val_2))

    def pop(self):
        if len(self.st) != 0:
            return self.st.pop()
        else:
            return [-1]

    def clear(self):
        self.st = []

    def size(self):
        return len(self.st)

    def __str__(self):
        str = ""
        for i in self.st:
            str += "({0} , {1}), ".format(i[0], i[1])
        str += "\n"
        return str
