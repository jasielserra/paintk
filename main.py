from tkinter import *
import pyscreenshot

class Paintk:
    def __init__(self):
        self.window = Tk()
        self.window.title("Paintk")
        self.window.minsize(width=1280, height=720)
        self.window.resizable(0,0)

        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

        self.img_line = PhotoImage(file="icons/icons/line.png")
        self.img_oval = PhotoImage(file="icons/icons/oval.png")
        self.img_eraser = PhotoImage(file="icons/icons/eraser.png")
        self.img_save = PhotoImage(file="icons/icons/save.png")
        self.img_square = PhotoImage(file="icons/icons/square.png")
        self.img_new = PhotoImage(file="icons/icons/new.png")

        self.colors = ("black","#3b3b3b","gray","white","red","green","blue", "purple","orange", "cyan", "yellow","cyan3")
        self.pick_colors = "black"

        self.bar_menu = Frame(self.window, bg='#3b3b3b', height=50)
        self.bar_menu.pack(fill="x")

        self.text_color = Label(self.bar_menu, text="  Color: ", fg="white", bg="#3b3b3b")
        self.text_color.pack(side="left")

        for color in self.colors:
            self.button_color = Button(self.bar_menu, bg=color, width=3, height=2, command=lambda col=color:self.select_colors(col)).pack(side="left")

        self.text_pen_size = Label(self.bar_menu, text="  Size:  ", fg="white", bg="#3b3b3b").pack(side="left")

        self.pen_size = Spinbox(self.bar_menu, from_=1, to=50)
        self.pen_size.pack(side="left")

        self.text_brushs = Label(self.bar_menu, text="  Brushs: ", fg="white", bg="#3b3b3b").pack(side="left")

        self.button_line = Button(self.bar_menu, image=self.img_line, bd=0, command=self.brush_line).pack(side="left")
        self.button_oval = Button(self.bar_menu, image=self.img_oval, bd=0, command=self.brush_oval).pack(side="left")
        self.button_eraser = Button(self.bar_menu, image=self.img_eraser, bd=0, command=self.brush_eraser).pack(side="left")

        self.text_options = Label(self.bar_menu, text="  Options:  ", fg="white", bg="#3b3b3b").pack(side="left")

        self.button_save = Button(self.bar_menu, image=self.img_save, bd=0, command=self.save).pack(side="left")
        self.button_new = Button(self.bar_menu, image=self.img_new, bd=0, command=self.clean).pack(side="left")

        self.area_draw = Canvas(self.window, height=720, bg="gainsboro")
        self.area_draw.pack(fill="both")
        self.area_draw.bind("<B1-Motion>", self.draw)

        self.window.mainloop()

    def draw(self, event):
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x), (event.y)

        if self.oval_brush:
            self.area_draw.create_oval(x1, y1, x2, y2, fill=self.pick_colors, outline=self.pick_colors, width=self.pen_size.get())

        elif self.line_brush:
            self.area_draw.create_line(x1 - 10, y1 -10, x2, y2, fill=self.pick_colors, width=self.pen_size.get())

        else:
            self.area_draw.create_oval(x1, y1, x2, y2, fill="gainsboro", outline="gainsboro", width=self.pen_size.get())


    def select_colors(self, col):
        self.pick_colors = col

    def brush_oval(self):
        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

    def brush_line(self):
        self.eraser_brush = False
        self.line_brush = True
        self.eraser_brush = False

    def brush_eraser(self):
        self.oval_brush = False
        self.line_brush = False
        self.eraser_brush = True

    def clean(self):
        self.area_draw.delete("all")

    def save(self):

        x = self.window.winfo_rootx() + self.area_draw.winfo_x()
        y = self.window.winfo_rooty() + self.area_draw.winfo_y()
        x1 = self.window.winfo_rootx() + self.area_draw.winfo_width()
        y1 = self.window.winfo_rooty() + self.area_draw.winfo_height()

        img = pyscreenshot.grab(bbox=(x, y, x1, y1))
        img.save("image.png", "png")

Paintk()