from tkinter import *
from tkinter import colorchooser

class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 6
        self.setUI()
        self.type = "oval"

    def exit(self):
        self.parent.quit()

    def set_color(self):
        (rgb, hx) = colorchooser.askcolor()
        self.color = hx

    def eraser(self):
        self.color = "white"

    def draw(self, event):
        if self.type == "line":
            self.canv.create_line(event.x - -3 * self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + 3 * self.brush_size,
                                  fill=self.color, width=4)
        if self.type == "reversed_line":
            self.canv.create_line(event.x - 3 * self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + 3 * self.brush_size,
                                  fill=self.color, width=4)
        if self.type == "oval":
            self.canv.create_oval(event.x - self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + self.brush_size,
                                  fill=self.color, outline=self.color)

    def on_scale(self, val):
        v = int(float(val))
        self.brush_size = v

    def change_oval(self):
        self.type = "oval"

    def change_line(self):
        self.type = "line"

    def change_reversed_line(self):
        self.type = "reversed_line"

    def setUI(self):

        self.parent.title("Plain Air")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6,
                             weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=10,
                       padx=5, pady=5,
                       sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>",
                       self.draw)

        color_btn = Button(self, text="Палитра", width=15, height=2,
                           command=lambda: self.set_color())
        color_btn.grid(row=0, column=0)

        color_btn = Button(self, text="Ластик", width=15, height=2,
                           command=lambda: self.eraser())
        color_btn.grid(row=0, column=1)

        size_lab = Label(self, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)

        scale = Scale(self, orient="horizontal",
                      from_=3, to=30,
                      command=self.on_scale)
        scale.grid(row=1, column=1, columnspan=3)

        clear_btn = Button(self, text="Удалить все", width=15, height=2,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=5)

        empty = Label(self, width=15)
        empty.grid(row=0, column=6)

        oval_btn = Button(self, text="Кисть: овал", width=15, height=2,
                          command=lambda: self.change_oval())
        oval_btn.grid(row=0, column=7)
        line_btn = Button(self, text="Кисть: перо", width=15, height=2,
                          command=lambda: self.change_line())
        line_btn.grid(row=0, column=8)
        reverse_line_btn = Button(self, text="Кисть: обратное перо", width=17, height=2,
                                  command=lambda: self.change_reversed_line())
        reverse_line_btn.grid(row=0, column=9)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Выход", command=self.exit)
        menubar.add_cascade(label="Файл", menu=fileMenu)


if __name__ == '__main__':
    root = Tk()
    root.geometry("850x500+300+300")
    app = Paint(root)
    root.mainloop()
