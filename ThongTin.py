from VeDat import VeDat
from datetime import datetime
from tkinter import *
from NhanVien import *
from tkinter import ttk,DISABLED,NORMAL,messagebox
from tk_tools import *
import tkinter.font as TkFont

def __init__(self, master, veDat):
        self.master = master
        self.veDat = veDat
        self.display()
def display(self):
        helv12 = TkFont.Font(family="Helvetica",size=12)

        nooteBook = ttk.Notebook(self.master)
        nooteBook.pack(anchor=CENTER)

        frame_thongTinKH = Frame(nooteBook,height=200,width=200)
        frame_thongTinKH.pack(fill="both",expand="TRUE")

        frame_thongTinVeDat = Frame(nooteBook,height=200,width=200)
        frame_thongTinVeDat.pack(fill="both",expand="TRUE")

        nooteBook.add(frame_thongTinKH,text="Thông tin khách hàng")
        nooteBook.add(frame_thongTinVeDat,text="Thông tin vé đặt")
        
        Label(frame_thongTinKH,text="maKH",font=helv12).grid(column=0,row=0,sticky=W)
        Label(frame_thongTinKH,text="Tên KH",font=helv12).grid(column=0,row=1,sticky=W)
        Label(frame_thongTinKH,text="CMND",font=helv12).grid(column=0,row=2,sticky=W)
        Label(frame_thongTinKH,text="Ngày Sinh",font=helv12).grid(column=0,row=3,sticky=W)
    

        Label(frame_thongTinKH,font=helv12,text=self.veDat.getmaKH()).grid(column=1,row=0,sticky=W)
        Label(frame_thongTinKH,font=helv12,text=self.veDat.gettenKH()).grid(column=1,row=1,sticky=W)
        Label(frame_thongTinKH,font=helv12,text=self.veDat.getCmnd()).grid(column=1,row=2,sticky=W)
        Label(frame_thongTinKH,font=helv12,text=self.veDat.getngaySinh()).grid(column=1,row=3,sticky=W)
        
        Label(frame_thongTinKH,text="",width=8).grid(column=0,row=5)

        Label(frame_thongTinVeDat,text="",width=8).grid(column=0,row=0)


        Button(frame_thongTinVeDat, text="maVe").grid(row=0,sticky=W,column=1)
        Button(frame_thongTinVeDat, text="Ngày đặt").grid(row=0,sticky=W,column=2)
        Button(frame_thongTinVeDat, text="Ngày hết hạn").grid(row=0,sticky=W,column=3)
        Button(frame_thongTinVeDat, text="Trạng Thái").grid(row=0,sticky=W,column=4)

        for i in self.VeDat:
                Label(frame_thongTinVeDat,font=helv12,text=self.veDat.maVe()).grid(column=1,row=0,sticky=W)
                Label(frame_thongTinVeDat,font=helv12,text=self.veDat.ngayDat()).grid(column=1,row=1,sticky=W)
                Label(frame_thongTinVeDat,font=helv12,text=self.veDat.ngayHetHan()).grid(column=1,row=2,sticky=W)
                Label(frame_thongTinVeDat,font=helv12,text=self.veDat.trangThai()).grid(column=1,row=3,sticky=W)
       
       
        Button(frame_thongTinKH, text="Hoàn Tất",command=self.hoanTat).grid(row=6,column=2,stick=E)
        self.master.geometry("300x200")
        self.master.mainloop()


        def hoanTat(self):
            self.trangThai =  True
            self.master.destroy()
    