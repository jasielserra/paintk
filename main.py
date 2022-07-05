from tkinter import *

class Paintk:
    def __init__(self):
        self.window = Tk()
        self.window.title("Paintk")
        self.window.minsize(width=1280, height=720)
        self.window.resizable(0,0)

        self.bar_menu = Frame(self.window, bg='#3b3b3b', height=50)
        self.bar_menu.pack(fill="x")

        self.area_draw = Canvas(self.window, height=720)
        self.area_draw.pack(fill="both")

        self.window.mainloop()

Paintk()