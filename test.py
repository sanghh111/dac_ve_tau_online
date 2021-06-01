from tkinter import *
from Ve import *

class a(Frame):
    def __init__(self,master):
        self.master=master
        self.ve=[]
        self.ve.append(Ve("SG-HN01-1"))
        self.display()
    def display(self):
        Label(self.master,text="Thanh Toán vé tàu",font=15).grid(column=0,columnspan=4,row=0)
        Label(self.master,text="Chuyến đi:",underline=True).grid(column=0,columnspan=3,row=1)
        Label(self.master,text=self.ve[0].getMaCD()).grid(column=1,columnspan=3,row=1)
        Label(self.master,text="Ga xuất phát:").grid(column=0,row=2,sticky=E)
        Label(self.master,text=self.ve[0].getGaDi()).grid(column=1,row=2,sticky=W)
        Label(self.master,text="Ga đến:").grid(column=2,row=2,sticky=E)
        Label(self.master,text=self.ve[0].getGaDen()).grid(column=3,row=2,sticky=E)
        Label(self.master,text="Thời gian:").grid(column=0,columnspan=3,row=3)
        Label(self.master,text=self.ve[0].getNgayKhoiHanh()).grid(column=1,row=3,columnspan=3)
        Label(self.master,text="Số ghế",width=6).grid(column=0,row=4,stick=W)
        Label(self.master,text="Tên toa",width=15).grid(column=1,row=4,stick=W)
        Label(self.master,text="Giá",width=10).grid(column=2,row=4,stick=W)
        self.master.mainloop()
a(Tk())