from tkinter import ttk
from PIL import Image,ImageTk


import tkinter as jra

class Application(jra.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        image = ImageTk.PhotoImage(Image.open("muiten.png").resize((600, 600), Image.ANTIALIAS))
        self.hi_there = jra.Button(self, image=image)
        self.hi_there["text"] = "Bắt đầu chạy chương trình"
        self.hi_there["command"] = self.PressCheck
        self.hi_there.pack()

        self.quit = jra.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

        self.pack()

    def PressCheck(self, event=None):
        print("hellu")



root = jra.Tk()
app = Application(master=root)
app.master.title("My checker app")
app.master.minsize(300, 200)
app.mainloop()

