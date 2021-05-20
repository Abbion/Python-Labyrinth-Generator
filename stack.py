class stack:
    def __init__(self):
        self.arr = []

    def push(self, val_1, val_2):
        self.arr.append((val_1, val_2))

    def clear(self):
        self.arr = []

    def size(self):
        return len(self.arr)

    def pop(self):
        if len(self.arr) != 0:
            return self.arr.pop()
        else:
            return [-1]

    def inv_pop(self):
        if len(self.arr) != 0:
            return self.arr.pop(0)
        else:
            return [-1]

    def print(self):
        for i in self.arr:
            print(i, end=' ')
        print()
