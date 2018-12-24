from tkinter import *
from vector import vector

class plot:
    def __init__(self, x, y):
        self.size = vector(300, 300)
        self.x = x
        self.y = y

        self._draw()

    def _draw(self):
        root = Tk()
        cPos = vector(self.x[0], self.y[0])
        w = Canvas(root, width = 300, height = 300)
        w.pack()
        i = 1
        while i < len(self.x):
            nPos = vector(self.x[i], self.y[i])
            w.create_line(cPos[0], cPos[1], nPos[0], nPos[1])
            cPos = nPos
            i += 1
        
        root.mainloop()



def test():
    x = []
    y = []
    for i in range(11):
        x.append(i*30)
        y.append(300*((i/10)**2))
    plot(x, y)

test()
