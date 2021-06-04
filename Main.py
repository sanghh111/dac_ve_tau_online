from VeDat import VeDat
from KhachHang import KhachHang
from re import A, L, T
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime, date
from typing import List, NewType
from db import *
from tkinter.constants import DISABLED, NORMAL
from Ve import Ve
# import threading


class App(Frame):
    def __init__(self, master):
        self.master = master
        self.title_dv = None
        self.title_tt = None
        self.title_tv = None
        self.title_tk = None
        self.label_dv = []
        self.label_tt = None
        self.label_tk = None
        self.cbb_dv = []
        self.entry_tt = None
        self.entry_tk = None
        self.button_tv = []
        self.button_dv = []
        self.button_tt = None
        self.button_tk = None
        self.spinbox = []
        self.ngay_dat_ve = datetime.now()
        # print(type(self.ngay_dat_ve.day))
        self.ngay = IntVar()
        self.thang = IntVar()
        self.nam = IntVar()
        self.ngay.set(self.ngay_dat_ve.day)
        self.thang.set(self.ngay_dat_ve.month)
        self.nam.set(self.ngay_dat_ve.year)
        self.line_dv = []
        self.trangThai = [None, None, None]
        self.con, self.cur = connect_DB('dac_ve_tau.db')
        self.giaTriGaDen = StringVar()
        self.giaTriGaDi = StringVar()
        self.display()

    def display(self):
        self.master.minsize(width=600, height=400)
        self.master.maxsize(width=600, height=400)
        self.master.resizable(1, 1)
        Button(self.master, text="Dac ve tau", command=self.dacVeTau,
               height=3, width=13).place(relx=0, rely=0)
        Button(self.master, text="Thanh Toan", command=self.thanhToan,
               width=15, height=3).place(relx=0.33, rely=0)
        Button(self.master, text="Tim kiem ve",
               command=self.timKiem).place(relx=0.66, rely=0)
        self.can = Canvas(self.master, bg='MediumPurple1', width=600, height=345,
                          highlightbackground='MediumPurple1', highlightthickness=0)
        self.can.place(x=0, y=55)
        # self.master.bind('<Motion>',self.location)
        self.master.mainloop()

    def dacVeTau(self):
        if(self.trangThai[0] == None and self.trangThai[2] == None):
            self.kiemTraTrangThai(0)
            self.tenGa = select_Ga(self.cur).fetchall()
            tenGa = []
            for i in self.tenGa:
                tenGa.append(i[1])
            self.tenGa.append(('Chọn', 'Chọn'))
            tenGa.append('chọn')
            self.giaTriGaDen.set('chọn')
            self.giaTriGaDi.set('chọn')
            self.trangThai[0] = 1
            for a in range(0, 2):
                self.label_dv.append([])
                self.cbb_dv.append([])
                self.button_dv.append([])
                self.line_dv.append([])
            for a in range(0, 3):
                self.spinbox.append([])  # spinbox [0]:day, [1]:month, [2]:year
            self.title_dv = Label(
                self.can, text="Dat ve tau", background='MediumPurple1')
            self.label_dv[0] = Label(
                self.can, text="Ga den", background='MediumPurple1')
            self.label_dv[1] = Label(
                self.can, text="Ga di", background='MediumPurple1')
            self.spinbox[0] = Spinbox(
                self.can, from_=1, to_=31, width=2, textvariable=self.ngay)
            self.spinbox[1] = Spinbox(self.can, from_=1, to_=12, width=2,
                                      textvariable=self.thang, command=self.thietLapGioiHanNgay)
            self.spinbox[2] = Spinbox(self.can, from_=2015, to_=2030, width=8,
                                      textvariable=self.nam, command=self.thietLapGioiHanNgay)
            self.button_dv[0] = Button(
                self.can, text="Tim Kiem", command=self.timVe)
            self.button_dv[1] = Button(
                self.can, text="Quay lai", command=self.quayLai_dv)
            self.cbb_dv[0] = ttk.Combobox(
                self.can, width=17, textvariable=self.giaTriGaDen, values=tenGa)
            self.cbb_dv[1] = ttk.Combobox(
                self.can, width=17, textvariable=self.giaTriGaDi, values=tenGa)
            self.label_dv[0].place(relx=0.1, rely=0.15)
            self.label_dv[1].place(relx=0.1, rely=0.25)
            self.cbb_dv[0].place(relx=0.2, rely=0.15)
            self.cbb_dv[1].place(relx=0.2, rely=0.25)
            self.spinbox[0].place(relx=0.2, rely=0.34)
            self.spinbox[1].place(relx=0.25, rely=0.34)
            self.spinbox[2].place(relx=0.3, rely=0.34)
            self.button_dv[0].place(relx=0.3, rely=0.42)
            self.button_dv[1].place(relx=0.2, rely=0.42)
            self.title_dv.place(relx=0.175, rely=0.065)
            self.line_dv[0] = self.can.create_line(-10, 180, 250, 180)
            self.line_dv[1] = self.can.create_line(250, -3, 250, 180)
        elif(self.trangThai[0] == 0):
            self.title_dv['text']="Đặt vé tàu"
            self.kiemTraTrangThai(0)
            self.trangThai[0] = 1
            self.hienThiDacVeTau()
        else:
            pass

    def thanhToan(self):
        if(self.trangThai[1] == None):
            self.kiemTraTrangThai(1)
            self.trangThai[1] = 1
            self.maVe = StringVar()
            self.title_tt = Label(
                self.can, text="Thanh toan ve tau", background='MediumPurple1')
            self.label_tt = Label(
                self.can, text="Ma dat truoc", background='MediumPurple1')
            self.entry_tt = Entry(self.can, textvariable=self.maVe)
            self.button_tt = Button(
                self.can, text="Tim kiem", command=self.timKiemVeDatTruoc)
            self.title_tt.place(relx=0.125, rely=0.065)
            self.label_tt.place(relx=0.05, rely=0.2)
            self.entry_tt.place(relx=0.175, rely=0.2)
            self.button_tt.place(relx=0.3, rely=0.4)
        elif(self.trangThai[1] == 0):
            self.kiemTraTrangThai(1)
            self.trangThai[1] = 1
            self.hienThiThanhToan()
        else:
            pass

    def timKiemVeDatTruoc(self):
        self.veDat = VeDat(self.maVe.get())
        if self.veDat.isNull():
            return
        else:
            try:
                self.labelTT
            except:
                self.labelTT = []
            Ve = Select_Ve_maVe(cur, self.veDat.get_maVe())
            print(Ve)
            if self.labelTT == []:
                self.labelTT.append(Label(self.can, text="THÔNG TIN VÉ"))
                self.labelTT.append(Label(self.can, text="Mã chuyến đi"))
                self.labelTT.append(Label(self.can, text="Ga xuất phát"))
                self.labelTT.append(Label(self.can, text="Ga đến"))
                self.labelTT.append(Label(self.can, text="Ngày đi"))
                self.btnTT = Button(self.can, text="Thanh toán",
                                    command=self.thanhToanVeDat)
                self.labelTT.append(Label(self.can, text=Ve[0]))
                self.labelTT.append(Label(self.can, text=Ve[1]))
                self.labelTT.append(Label(self.can, text=Ve[2]))
                self.labelTT.append(Label(self.can, text=Ve[3]))
                self.labelTT[0].place(relx=0.65, rely=0.1)
                self.labelTT[1].place(relx=0.55, rely=0.175)
                self.labelTT[2].place(relx=0.5, rely=0.25)
                self.labelTT[3].place(relx=0.8, rely=0.25)
                self.labelTT[4].place(relx=0.60, rely=0.325)
                self.labelTT[5].place(relx=0.7, rely=0.175)
                self.labelTT[6].place(relx=0.63, rely=0.25)
                self.labelTT[7].place(relx=0.88, rely=0.25)
                self.labelTT[8].place(relx=0.7, rely=0.325)
                self.btnTT.place(relx=0.85, rely=0.4)
            else:
                self.labelTT[0].place(relx=0.65, rely=0.1)
                self.labelTT[1].place(relx=0.55, rely=0.175)
                self.labelTT[2].place(relx=0.5, rely=0.25)
                self.labelTT[3].place(relx=0.8, rely=0.25)
                self.labelTT[4].place(relx=0.60, rely=0.325)
                self.labelTT[5].place(relx=0.7, rely=0.175)
                self.labelTT[6].place(relx=0.63, rely=0.25)
                self.labelTT[7].place(relx=0.88, rely=0.25)
                self.labelTT[8].place(relx=0.7, rely=0.325)
                self.btnTT.place(relx=0.85, rely=0.4)

    def thanhToanVeDat(self):
        kh = KhachHang()
        kh.setmaKH(self.veDat.get_kh())
        UIThanhToan(Toplevel(),dsMaVe=self.veDat.get_maVe(),kh=kh,object=self,trangThai=False)

    def timKiem(self):
        if(self.trangThai[2] == None and self.trangThai[0] == None):
            self.kiemTraTrangThai(2)
            self.tenGa = select_Ga(self.cur).fetchall()
            tenGa = []
            for i in self.tenGa:
                tenGa.append(i[1])
            self.tenGa.append(('Chọn', 'Chọn'))
            tenGa.append('chọn')
            self.giaTriGaDen.set('chọn')
            self.giaTriGaDi.set('chọn')
            self.trangThai[2] = 1
            for a in range(0, 2):
                self.label_dv.append([])
                self.cbb_dv.append([])
                self.button_dv.append([])
                self.line_dv.append([])
            for a in range(0, 3):
                self.spinbox.append([])  # spinbox [0]:day, [1]:month, [2]:year
            self.title_dv = Label(
                self.can, text="Tìm kiếm vé tàu", background='MediumPurple1')
            self.label_dv[0] = Label(
                self.can, text="Ga den", background='MediumPurple1')
            self.label_dv[1] = Label(
                self.can, text="Ga di", background='MediumPurple1')
            self.spinbox[0] = Spinbox(
                self.can, from_=1, to_=31, width=2, textvariable=self.ngay)
            self.spinbox[1] = Spinbox(self.can, from_=1, to_=12, width=2,
                                      textvariable=self.thang, command=self.thietLapGioiHanNgay)
            self.spinbox[2] = Spinbox(self.can, from_=2015, to_=2030, width=8,
                                      textvariable=self.nam, command=self.thietLapGioiHanNgay)
            self.button_dv[0] = Button(
                self.can, text="Tim Kiem", command=self.timVe)
            self.button_dv[1] = Button(
                self.can, text="Quay lai", command=self.quayLai_dv)
            self.cbb_dv[0] = ttk.Combobox(
                self.can, width=17, textvariable=self.giaTriGaDen, values=tenGa)
            self.cbb_dv[1] = ttk.Combobox(
                self.can, width=17, textvariable=self.giaTriGaDi, values=tenGa)
            self.label_dv[0].place(relx=0.1, rely=0.15)
            self.label_dv[1].place(relx=0.1, rely=0.25)
            self.cbb_dv[0].place(relx=0.2, rely=0.15)
            self.cbb_dv[1].place(relx=0.2, rely=0.25)
            self.spinbox[0].place(relx=0.2, rely=0.34)
            self.spinbox[1].place(relx=0.25, rely=0.34)
            self.spinbox[2].place(relx=0.3, rely=0.34)
            self.button_dv[0].place(relx=0.3, rely=0.42)
            self.button_dv[1].place(relx=0.2, rely=0.42)
            self.title_dv.place(relx=0.175, rely=0.065)
            self.line_dv[0] = self.can.create_line(-10, 180, 250, 180)
            self.line_dv[1] = self.can.create_line(250, -3, 250, 180)
        else:
            self.title_dv['text']="Tìm kiếm vé tàu"
            self.kiemTraTrangThai(2)
            self.trangThai[2] = 1
            self.hienThiDacVeTau()

    def timVe(self):
        self.xoaCanTV()
        ngayThangNam = str(self.nam.get())+"-"
        if(self.thang.get() < 10):
            ngayThangNam += "0"+str(self.thang.get())
        else:
            ngayThangNam += str(self.thang.get())
        ngayThangNam += "-"
        if(self.ngay.get() < 10):
            ngayThangNam += "0"+str(self.ngay.get())
        else:
            ngayThangNam += str(self.ngay.get())
        self.ket_qua = select_CD(
            self.cur, ngayThangNam, self.tenGa[self.cbb_dv[0].current()][0], self.tenGa[self.cbb_dv[1].current()][0])
        if(self.ket_qua):
            self.ket_qua = self.ket_qua.fetchall()
        self.label_stt = []
        self.label_maSo = []
        self.label_gaDi = []
        self.label_gaDen = []
        self.label_ngayDi = []
        self.radbu_timVe = []
        self.giaTri_radbu = []
        if(self.title_tv == None):
            self.line_danhSachVe = []
            self.title_tv = Label(
                self.can, text='Danh sach dat ve', background='thistle1')
            for i in range(10):
                self.line_dv.append([])
            for i in range(6):
                self.button_tv.append([])
            self.line_dv[2] = self.can.create_line(250, 180, 600, 180)
            self.line_dv[3] = self.can.create_line(250, 45, 600, 45)
            self.line_dv[4] = self.can.create_line(250, 70, 600, 70)
            self.button_tv[0] = Button(self.can, text="Stt", height=1, width=3)
            self.button_tv[1] = Button(
                self.can, text="Mã số", height=1, width=8)
            self.button_tv[2] = Button(
                self.can, text="Ga đi", height=1, width=8)
            self.button_tv[3] = Button(
                self.can, text="Ga đến", height=1, width=8)
            self.button_tv[4] = Button(
                self.can, text="Ngay đi", height=1, width=8)
            self.button_tv[5] = Button(self.can, height=1, width=7)
            self.button_next = Button(self.can, text='Next')
            self.button_back = Button(self.can, text='Back')
            self.can_tv = Canvas(self.can, height=110,
                                 width=350, highlightthickness=0)
            """
            ,bg='MediumPurple1',highlightbackground='MediumPurple1'
            """
            self.themDanhSachVe()
            self.title_tv.place(relx=0.6, rely=0.065)
            self.button_tv[0].place(x=250, y=45)
            self.button_tv[1].place(x=280, y=45)
            self.button_tv[2].place(x=345, y=45)
            self.button_tv[3].place(x=410, y=45)
            self.button_tv[4].place(x=475, y=45)
            self.button_tv[5].place(x=540, y=45)
            self.can_tv.place(x=251, y=70)
        elif(self.title_tv.grid_info() == {}):
            self.themDanhSachVe()
            self.title_tv.place(relx=0.6, rely=0.065)
            self.line_dv[2] = self.can.create_line(250, 180, 600, 180)
            self.line_dv[3] = self.can.create_line(250, 45, 600, 45)
            self.line_dv[4] = self.can.create_line(250, 70, 600, 70)
            self.button_tv[0].place(x=250, y=45)
            self.button_tv[1].place(x=280, y=45)
            self.button_tv[2].place(x=345, y=45)
            self.button_tv[3].place(x=410, y=45)
            self.button_tv[4].place(x=475, y=45)
            self.button_tv[5].place(x=540, y=45)
            self.can_tv.place(x=251, y=70)

    def quayLai_dv(self):
        self.title_dv.place_forget()
        print(self.title_dv.place_info())

    def kiemTraTrangThai(self, trangThai):
        if(self.trangThai[trangThai] == 1):
            return
        for i in range(len(self.trangThai)):
            if(self.trangThai[i] == 1):
                self.trangThai[i] = 0
                if(i == 0):
                    self.title_dv.place_forget()
                    for i in self.label_dv:
                        i.place_forget()
                    for i in self.cbb_dv:
                        i.place_forget()
                    for i in self.spinbox:
                        i.place_forget()
                    for i in self.button_dv:
                        i.place_forget()
                    for i in range(2):
                        self.can.delete(self.line_dv[i])
                    self.xoaCanTV()
                    try:
                        self.trangThaiToa
                    except:
                        self.trangThaiToa = False
                    if(self.trangThaiToa):
                        self.loadLaiHienThiTau()
                    # elif(self.title_tv.place_info() != {}):
                    #     self.title_tv.place_forget()
                    #     for i in self.label_dv:
                    #         i.place_forget()
                    #     for i in self.button_tv:
                    #         i.place_forget()
                    #     self.can_tv.place_forget()
                elif(i == 1):
                    self.title_tt.place_forget()
                    self.label_tt.place_forget()
                    self.entry_tt.place_forget()
                    self.button_tt.place_forget()
                    try:
                        self.veDat
                    except:
                        self.veDat = None
                    if self.veDat != None:
                        for i in self.labelTT:
                            i.place_forget()
                        self.btnTT.place_forget()
                    try:
                        del(self.veDat)
                    except:
                        print("Khong co ve dat")
                elif(i == 2):
                    self.title_dv.place_forget()
                    for i in self.label_dv:
                        i.place_forget()
                    for i in self.cbb_dv:
                        i.place_forget()
                    for i in self.spinbox:
                        i.place_forget()
                    for i in self.button_dv:
                        i.place_forget()
                    for i in range(2):
                        self.can.delete(self.line_dv[i])
                    self.xoaCanTV()
                    try:
                        self.trangThaiToa
                    except:
                        self.trangThaiToa = False
                    if(self.trangThaiToa):
                        self.loadLaiHienThiTau()
        return

    def xoaCanTV(self):
        try:
            self.title_tv
        except:
            self.title_tv = None
        if(self.title_tv):
            if(self.title_tv.place_info() == {}):
                print("khong co")
                pass
            else:
                print("xoa")
                self.title_tv.place_forget()
                for i in range(2, len(self.line_dv)):
                    self.can.delete(self.line_dv[i])
                for i in self.button_tv:
                    i.place_forget()
                self.can_tv.place_forget()
                if(self.ket_qua != []):
                    for i in self.label_stt:
                        i.place_forget()
                    for i in self.label_maSo:
                        i.place_forget()
                    for i in self.label_gaDi:
                        i.place_forget()
                    for i in self.label_gaDen:
                        i.place_forget()
                    for i in self.label_ngayDi:
                        i.place_forget()
                    for i in self.radbu_timVe:
                        i.place_forget()
                    self.line_danhSachVe.clear()
                    self.label_stt.clear()
                    self.label_maSo.clear()
                    self.label_gaDi.clear()
                    self.label_gaDen.clear()
                    self.label_ngayDi.clear()
                    self.radbu_timVe.clear()
                    self.giaTri_radbu.clear()
                pass
        pass

    def hienThiDacVeTau(self):
        self.label_dv[0].place(relx=0.1, rely=0.15)
        self.label_dv[1].place(relx=0.1, rely=0.25)
        self.cbb_dv[0].place(relx=0.2, rely=0.15)
        self.cbb_dv[1].place(relx=0.2, rely=0.25)
        self.spinbox[0].place(relx=0.2, rely=0.34)
        self.spinbox[1].place(relx=0.25, rely=0.34)
        self.spinbox[2].place(relx=0.3, rely=0.34)
        self.button_dv[0].place(relx=0.3, rely=0.42)
        self.button_dv[1].place(relx=0.2, rely=0.42)
        self.title_dv.place(relx=0.175, rely=0.065)
        self.line_dv[0] = self.can.create_line(-10, 180, 250, 180)
        self.line_dv[1] = self.can.create_line(250, -3, 250, 180)

    def hienThiThanhToan(self):
        self.title_tt.place(relx=0.125, rely=0.065)
        self.label_tt.place(relx=0.05, rely=0.2)
        self.entry_tt.place(relx=0.175, rely=0.2)
        self.button_tt.place(relx=0.3, rely=0.4)

    def hienThiTimKiemVe(self):
        self.title_tk.place(relx=0.125, rely=0.065)
        self.label_tk.place(relx=0.05, rely=0.2)
        self.entry_tk.place(relx=0.175, rely=0.2)
        self.button_tk.place(relx=0.3, rely=0.4)

    def thietLapGioiHanNgay(self):
        if(self.thang.get() in [2, 4, 6, 9, 11]):
            if(self.thang.get() == 2):
                if(self.nam.get() % 4 == 0):
                    if(self.ngay.get() > 29):
                        self.ngay.set(29)
                    self.spinbox[0].configure(to_=29)
                else:
                    if(self.ngay.get() > 28):
                        self.ngay.set(28)
                    self.spinbox[0].configure(to_=28)
            else:
                if(self.ngay.get() > 30):
                    self.ngay.set(30)
                    self.spinbox[0].configure(to_=30)
        else:
            self.spinbox[0].configure(to_=31)
        pass

    def themDanhSachVe(self):
        Y = 0
        self.giaTriChon = IntVar()
        for i in range(len(self.ket_qua)):
            self.line_danhSachVe.append([])
            self.label_stt.append(None)
            self.label_maSo.append(None)
            self.label_gaDi.append(None)
            self.label_gaDen.append(None)
            self.label_ngayDi.append(None)
            self.radbu_timVe.append(None)
            self.giaTri_radbu.append(None)
        for i in range(len(self.line_danhSachVe)):
            for j in range(7):
                self.line_danhSachVe[i].append(None)
        for i in range(len(self.line_danhSachVe)):
            self.line_danhSachVe[i][0] = self.can_tv.create_line(
                29, Y, 29, Y+27)  # stt
            self.line_danhSachVe[i][1] = self.can_tv.create_line(
                93, Y, 93, Y+27)  # maSo
            self.line_danhSachVe[i][2] = self.can_tv.create_line(
                158, Y, 158, Y+30)  # gaDi
            self.line_danhSachVe[i][3] = self.can_tv.create_line(
                223, Y, 223, Y+30)  # gaDen
            self.line_danhSachVe[i][4] = self.can_tv.create_line(
                288, Y, 288, Y+30)  # ngayDi
            self.line_danhSachVe[i][5] = self.can_tv.create_line(
                347, Y, 347, Y+30)  # Button
            self.line_danhSachVe[i][6] = self.can_tv.create_line(
                0, Y+30, 347, Y+30)
            self.label_stt[i] = Label(
                self.can_tv, text=str(i+1), highlightthickness=0)
            self.label_stt[i].place(x=7, y=0+Y+3)
            self.label_maSo[i] = Label(
                self.can_tv, text=self.ket_qua[i][0], highlightthickness=0, width=8)
            self.label_maSo[i].place(x=31, y=0+Y+3)
            self.label_gaDi[i] = Label(
                self.can_tv, text=self.ket_qua[i][1], highlightthickness=0, width=8)
            self.label_gaDi[i].place(x=95, y=0+Y+3)
            self.label_gaDen[i] = Label(
                self.can_tv, text=self.ket_qua[i][2], highlightthickness=0, width=8)
            self.label_gaDen[i].place(x=160, y=0+Y+3)
            self.label_ngayDi[i] = Label(
                self.can_tv, text=self.ket_qua[0][3], highlightthickness=0, width=8)
            self.label_ngayDi[i].place(x=225, y=0+Y+3)
            self.giaTri_radbu[i] = i
            self.radbu_timVe[i] = Radiobutton(
                self.can_tv, value=self.giaTri_radbu[i], variable=self.giaTriChon, command=self.onClick, highlightthickness=0)
            self.radbu_timVe[i].place(x=305, y=0+Y+3)
            Y += 30

    def onClick(self):
        self.thongTinVe = Select_Ve(
            self.cur, self.ket_qua[self.giaTriChon.get()][0])
        try:
            self.trangThaiToa
        except:
            self.trangThaiToa = False
        if(self.trangThaiToa):
            self.tatDanhSachDatVe()
        self.loadLaiHienThiTau()
        if(self.thongTinVe != []):
            self.viTritoa = 0
            self.hienThiToaTau()
        else:
            print("không có")
            pass

    def hienThiToaTau(self):
        self.trangThaiToa = True
        if(self.viTritoa == 0):
            self.btnToaBack = Button(
                self.can, text="trang trước", highlightthickness=0, command=self.backToa)
            self.btnToaNext = Button(
                self.can, text="trang tiếp", highlightthickness=0, command=self.nextToa)
            self.title_toa = Label(self.can, text="", width=30)
            chuoi = (self.thongTinVe[0][2]+"-" +
                     str(self.thongTinVe[0][4])+"VND")
            self.title_toa['text'] = chuoi
            self.btnToaBack.place(x=0, y=252)
            self.btnToaNext.place(x=567, y=252)
            self.title_toa.place(x=200, y=205)
            hcn1 = self.can.create_rectangle(40, 200, 560, 325)
            hcn2 = self.can.create_rectangle(60, 210, 540, 315)
            try:
                self.line_toa[0] = hcn1
            except:
                self.line_toa.append(hcn1)
            try:
                self.line_toa[1] = hcn2
            except:
                self.line_toa.append(hcn2)
            for i in range(16):
                for j in range(4):
                    dem = i*4+j+1
                    a = Button(self.can, text=dem, bg='blue',
                               highlightthickness=0, width=2)
                    a['command'] = self.callBackOnClickChoNgoi(
                        btn=a, dem=dem, ten='Ngồi mềm điều hòa')
                    a.place(x=75+i*29, y=230+j*20)
                    print('self.trangThai[2]: ', self.trangThai[2])
                    if(self.trangThai[2] == 1):
                        a["state"] = DISABLED
                    if(self.thongTinVe[dem-1][3] == "Trống"):
                        try:
                            self.button_ve[dem-1] = a
                        except:
                            self.button_ve.append(a)
                    else:
                        a["state"] = DISABLED
                        a["bg"] = 'red'
                        try:
                            self.button_ve[dem-1] = a
                        except:
                            self.button_ve.append(a)
                line_toa = self.can.create_line(74+i*29, 230, 74+i*29, 310)
                try:
                    self.line_toa[i+2] = line_toa
                except:
                    self.line_toa.append(line_toa)
        elif(self.viTritoa == 1):
            self.btnToaBack.place(x=0, y=252)
            self.btnToaNext.place(x=567, y=252)
            self.title_toa.place(x=200, y=205)
            try:
                self.line_toa[0] = self.can.create_rectangle(40, 200, 560, 325)
                self.line_toa[1] = self.can.create_rectangle(45, 210, 555, 315)
            except:
                self.line_toa.append(
                    self.can.create_rectangle(40, 200, 560, 325))
                self.line_toa.append(
                    self.can.create_rectangle(45, 210, 555, 315))
            chuoi = (self.thongTinVe[64][2]+"-" +
                     str(self.thongTinVe[64][4])+"VND")
            self.title_toa['text'] = chuoi
            for i in range(20):
                for j in range(4):
                    dem = i*4+j+1
                    a = Button(self.can, text=dem, bg='blue',
                               highlightthickness=0, width=2)
                    a.place(x=53+i*25, y=230+j*20)
                    a['command'] = self.callBackOnClickChoNgoi(
                        btn=a, dem=dem, ten='Ngồi cứng điều hòa')
                    if(self.thongTinVe[dem-1+64][3] == "Trống"):
                        try:
                            self.button_ve[dem-1+64] = a
                        except:
                            self.button_ve.append(a)
                    else:
                        a["state"] = DISABLED
                        a["bg"] = 'red'
                        try:
                            self.button_ve[dem-1+64] = a
                        except:
                            self.button_ve.append(a)
                line_toa = self.can.create_line(52+i*25, 230, 52+i*25, 310)
                try:
                    self.line_toa[i+2] = line_toa
                except:
                    self.line_toa.append(line_toa)
        elif(self.viTritoa == 2):  # bien dem cho line
            chuoi = (self.thongTinVe[144][2]+"-" +
                     str(self.thongTinVe[144][4])+"VND")
            self.title_toa['text'] = chuoi
            self.btnToaBack.place(x=0, y=252)
            self.btnToaNext.place(x=567, y=252)
            self.title_toa.place(x=200, y=205)
            try:
                self.line_toa[0] = self.can.create_rectangle(40, 200, 560, 325)
                self.line_toa[1] = self.can.create_rectangle(60, 210, 540, 315)
            except:
                self.line_toa.append(
                    self.can.create_rectangle(40, 200, 560, 325))
                self.line_toa.append(
                    self.can.create_rectangle(60, 210, 540, 315))
            for i in range(11):
                for j in range(2):
                    dem = i*2+j+1
                    print(dem)
                    a = Button(self.can, text=dem, bg='blue',
                               highlightthickness=0, width=2)
                    a['command'] = self.callBackOnClickChoNgoi(
                        btn=a, dem=dem, ten='Toa 4 chiều')
                    a.place(x=63+i*35, y=230+j*40)
                    if(self.thongTinVe[dem-1+144][3] == "Trống"):
                        try:
                            self.button_ve[dem-1+144] = a
                        except:
                            self.button_ve.append(a)
                    else:
                        a["state"] = DISABLED
                        a["bg"] = 'red'
                        try:
                            self.button_ve[dem-1] = a
                        except:
                            self.button_ve.append(a)
                    line_toa = self.can.create_line(
                        62+i*35, 230+j*40, 62+i*35, 260+j*40)
                    try:
                        self.line_toa[i*2+j+3] = line_toa
                    except:
                        self.line_toa.append(line_toa)
        elif(self.viTritoa == 3):  # bien dem cho line
            chuoi = (self.thongTinVe[168][2]+"-" +
                     str(self.thongTinVe[172][4])+"VND")
            self.title_toa['text'] = chuoi
            self.btnToaBack.place(x=0, y=252)
            self.btnToaNext.place(x=567, y=252)
            self.title_toa.place(x=200, y=205)
            self.line_toa.append(self.can.create_rectangle(40, 200, 560, 325))
            self.line_toa.append(self.can.create_rectangle(60, 210, 540, 315))
            for i in range(14):
                for j in range(3):
                    dem = i*3+j+1
                    a = Button(self.can, text=dem, bg='blue',
                               highlightthickness=0, width=2)
                    a['command'] = self.callBackOnClickChoNgoi(
                        btn=a, dem=dem, ten='Toa 6 chiều')
                    a.place(x=63+i*35, y=230+j*40)
                    if(self.thongTinVe[dem-1+172][3] == "Trống"):
                        try:
                            self.button_ve[dem-1+172] = a
                        except:
                            self.button_ve.append(a)
                    else:
                        a["state"] = DISABLED
                        a["bg"] = 'red'
                        try:
                            self.button_ve[dem-1] = a
                        except:
                            self.button_ve.append(a)
                    line_toa = self.can.create_line(
                        62+i*35, 230+j*40, 62+i*35, 260+j*40)
                    try:
                        self.line_toa[i+2] = line_toa
                    except:
                        self.line_toa.append(line_toa)

    def location(self, event):
        print(event.x, event.y)

    def nextToa(self):
        if(self.viTritoa < 3):
            print("next")
            self.loadLaiHienThiTau()
            self.viTritoa += 1
            self.hienThiToaTau()

    def backToa(self):
        if(self.viTritoa > 0):
            self.loadLaiHienThiTau()
            self.viTritoa -= 1
            self.hienThiToaTau()

    def loadLaiHienThiTau(self):
        try:
            self.title_toa
        except:
            self.title_toa = None
            self.button_ve = []
            self.line_toa = []
        if(self.title_toa != None):
            self.title_toa.place_forget()
            self.title_toa['text'] = ""
            self.btnToaBack.place_forget()
            self.btnToaNext.place_forget()
            for i in self.button_ve:
                i.place_forget()
            for i in self.line_toa:
                self.can.delete(i)

    def callBackOnClickChoNgoi(self, **kw):
        def __callback():
            return self.onClickChoNgoi(kw)
        return __callback

    def onClickChoNgoi(self, kw):
        self.taoViewDSC()
        if kw['ten'] == 'Ngồi mềm điều hòa':
            heso = 0
        elif kw['ten'] == 'Ngồi cứng điều hòa':
            heso = 64
        elif kw['ten'] == 'Toa 4 chiều':
            heso = 64+80
        elif kw['ten'] == 'Toa 6 chiều':
            heso = 80+64+24
        if((kw['dem'], kw['ten']) in self.DSC):
            print("Co ghe: ", self.DSC.index((kw['dem'], kw['ten'])))
            self.ViewDSC.xoaGhe(self.DSC.index((kw['dem'], kw['ten'])))
            self.DSC.remove((kw['dem'], kw['ten']))
            self.button_ve[kw['dem']+heso-1]['bg'] = 'blue'
        else:
            print("chua co")
            self.DSC.append((kw['dem'], kw['ten']))
            self.ViewDSC.themGhe(kw['dem'], kw['ten'],
                                 self.thongTinVe[kw['dem']-1][4])
            self.button_ve[kw['dem']-1+heso]['bg'] = 'RosyBrown3'

    def nhanTinHieu(self, **kw):
        return kw['object']

    def tatDanhSachDatVe(self):
        pass

    def taoViewDSC(self):
        try:

            self.ViewDSC
        except:
            self.ViewDSC = None
        if(self.ViewDSC == None):
            self.ViewDSC = DanhSachVe(Toplevel(), object=self)
            self.DSC = []

    def setMVDSC(self):
        self.maVeDSC = []
        for i in self.DSC:
            heSo = int()
            if i[1] == 'Ngồi mềm điều hòa':
                heSo = 0
            elif i[1] == 'Ngồi cứng điều hòa':
                heSo = 64
            elif i[1] == 'Toa 4 chiều':
                heSo = 64+80
            elif i[1] == 'Toa 6 chiều':
                heSo = 80+64+24
            self.maVeDSC.append(self.thongTinVe[heSo+i[0]-1][0])

    def thanhToanDV(self, kh):
        # self.maVeDSC()
        UIThanhToan(Toplevel(), kh=kh, object=self,
                    trangThai=True, dsMaVe=self.maVeDSC)


class DanhSachVe(Frame):
    def __init__(self, master, **kw):
        self.master = master
        self.kw = kw['object']
        self.guiTinHieu(kw)
        self.lbGhe = []
        self.kh = None
        self.display()

    def display(self):
        Label(self.master, text='DANH SÁCH VÉ CHỌN').grid(
            column=0, columnspan=4, row=0)
        Label(self.master, text="Số ghế", bg="blue",
              width=10).grid(column=0, row=1, sticky=W)
        Label(self.master, text="Tên toa", bg="LightSteelBlue2",
              width=20).grid(column=1, row=1, sticky=W)
        Label(self.master, text="Giá", bg="red", width=20).grid(
            column=2, row=1, sticky=W)
        self.btnDV = Button(self.master, text="Đặt Vé", command=self.datVe)
        self.demRow = 2
        self.master.mainloop

    def guiTinHieu(self, kw):
        kw['object'].nhanTinHieu(object=self)

    def themGhe(self, soGhe, tenToa, gia):
        tam1 = Label(self.master, text=soGhe)
        tam1.grid(column=0, row=self.demRow)
        tam2 = Label(self.master, text=tenToa)
        tam2.grid(column=1, row=self.demRow)
        tam3 = Label(self.master, text=gia)
        tam3.grid(column=2, row=self.demRow)
        if(self.btnDV.grid_info() != {}):
            self.btnDV.grid_forget()
        self.btnDV.grid(column=3, row=self.demRow+1, sticky=W)
        self.demRow += 1
        self.lbGhe.append((tam1, tam2, tam3))
        pass

    def xoaGhe(self, viTri):
        a = self.lbGhe[viTri]
        a[0].grid_forget()
        a[1].grid_forget()
        a[2].grid_forget()
        self.btnDV.grid_forget()
        print("self.demRow=", self.demRow)
        for i in range(viTri, self.demRow-3):
            # print(i)
            self.lbGhe[i+1][0].grid_forget()
            self.lbGhe[i+1][1].grid_forget()
            self.lbGhe[i+1][2].grid_forget()
            self.lbGhe[i+1][0].grid(column=0, row=i+2)
            self.lbGhe[i+1][1].grid(column=1, row=i+2)
            self.lbGhe[i+1][2].grid(column=2, row=i+2)
        self.btnDV.grid(column=3, row=self.demRow, sticky=W)
        self.demRow -= 1
        self.lbGhe.remove(a)

    def datVe(self):
        a = messagebox.askquestion(
            "Đặt vé tàu", "Bạn có muốn đặt vé tàu không?")
        # print(a)
        if a == 'yes':
            DSC = self.kw.setMVDSC()
            del(self.kw.ViewDSC)
            del(self.kw.DSC)
            self.kw.loadLaiHienThiTau()
            UIThongTinKH(Toplevel(), object=self.kw)
            self.master.destroy()
        if a == 'no':
            pass

    def __del__(self):
        pass
        # del(self.kw.ViewDSC)
        # del(self.kw.DCS)


class UIThongTinKH(Frame):
    def __init__(self, master, **kw):
        self.master = master
        if('object' in kw):
            self.kw = kw['object']
            # self.nhanTinHieu()
        self.kh = KhachHang()
        self.value = [StringVar(), StringVar(),
                      IntVar(), IntVar(), IntVar()]
        self.ngay = []
        self.thang = []
        self.nam = []
        for i in range(1, 32):
            self.ngay.append(i)
        for i in range(1, 13):
            self.thang.append(i)
        for i in range(1950, 2022):
            self.nam.append(i)
        self.display()

    def display(self):
        Label(self.master, text="NHẬP THÔNG TIN KHÁCH HÀNG").grid(
            column=0, columnspan=4, row=0)
        ten = Label(self.master, text="Tên")
        tuoi = Label(self.master, text="Tuổi")
        cmnd = Label(self.master, text="CMND")
        ngaySinh = Label(self.master, text="Ngày sinh")
        ten.grid(column=0, row=1, sticky=W)
        # tuoi.grid(column=0, row=2, sticky=W)
        cmnd.grid(column=0, row=2, sticky=W)
        ngaySinh.grid(column=0, row=3, sticky=W)
        Entry(self.master, textvariable=self.value[0]).grid(column=1, row=1)
        Entry(self.master, textvariable=self.value[1]).grid(column=1, row=2)
        # Entry(self.master, textvariable=self.value[2]).grid(column=1, row=3)
        ttk.Combobox(self.master, textvariable=self.value[2], value=self.ngay, width=5).grid(
            column=2, row=3, sticky=E)
        ttk.Combobox(self.master, textvariable=self.value[3], value=self.thang, width=5).grid(
            column=3, row=3)
        ttk.Combobox(self.master, textvariable=self.value[4], value=self.nam, width=10).grid(
            column=4, row=3)
        # them(ten =ten,tuoi=tuoi,cmnd=cmnd)
        Button(self.master, text="Xác nhận",
               command=self.onClick).grid(column=4, row=4)
        self.trangThai = Label(self.master, text="Nhập thiếu thuộc tính")
        self.master.mainloop

    def __del__(self):
        print("hello")

    def onClick(self):
        for i in self.value:
            if i.get() == '' or i.get() == 0:
                self.trangThai.grid(column=0, columnspan=3, row=4, sticky=E)
                return
        self.kh.setTenKH(self.value[0].get())
        self.kh.setCMND(self.value[1].get())
        self.kh.setNgaySinh(self.value[2].get(),
                            self.value[3].get(),
                            self.value[4].get())
        self.master.destroy()
        self.kw.thanhToanDV(self.kh)

    def __del__(self):
        # self.kw.setdsKH(self.kh)
        pass


class UIThanhToan(Frame):
    def __init__(self, master, **kw):
        # super.__init__()
        if 'object' in kw:
            self.object = kw['object']
        if 'trangThai' in kw:
            self.trangThai = kw['trangThai']
        if 'kh' in kw:
            self.kh = kw['kh']
        if 'dsMaVe' in kw:
            self.dsMaVe = kw['dsMaVe']
        print('self.kh: ', self.kh)
        # print('self.dsMaVe: ', self.dsMaVe)
        self.ve = []
        
        try:
            for i in self.dsMaVe:
                self.ve.append(Ve(i))
        except:
            self.ve.append(Ve(self.dsMaVe))
        self.master = master
        self.display()

    def display(self):
        Label(self.master, text="Thanh Toán vé tàu", font=15).grid(
            column=0, columnspan=4, row=0)
        Label(self.master, text="Chuyến đi").grid(
            column=0, columnspan=3, row=1)
        Label(self.master, text=self.ve[0].getMaCD()).grid(
            column=1, columnspan=3, row=1)
        Label(self.master, text="Ga xuất phát").grid(column=0, row=2, sticky=E)
        Label(self.master, text=self.ve[0].getGaDi()).grid(
            column=1, row=2, sticky=W)
        Label(self.master, text="Ga đến").grid(column=2, row=2, sticky=E)
        Label(self.master, text=self.ve[0].getGaDen()).grid(
            column=3, row=2, sticky=E)
        Label(self.master, text="Thời gian").grid(
            column=0, columnspan=3, row=3)
        Label(self.master, text=self.ve[0].getNgayKhoiHanh()).grid(
            column=1, row=3, columnspan=3)
        Label(self.master, text="Số ghế", width=5).grid(
            column=0, row=4)
        Label(self.master, text="Tên toa", width=20).grid(
            column=1, row=4)
        Label(self.master, text="Giá", width=10).grid(column=2, row=4)
        self.drow = 5
        tongGiaVe = 0
        for i in self.ve:
            Label(self.master, text=i.getSoGhe(), width=10).grid(
                column=0, row=self.drow)
            Label(self.master, text=i.getTenToa(), width=20).grid(
                column=1, row=self.drow)
            Label(self.master, text=i.getGia(), width=10).grid(
                column=2, row=self.drow)
            tongGiaVe += i.getGia()
            self.drow += 1
        Label(self.master, text="Tổng tiền:").grid(
            column=1, row=self.drow, sticky=E)
        Label(self.master, text=tongGiaVe).grid(
            column=2, row=self.drow, stick=W)
        if self.trangThai:
            Button(self.master, text="Thanh toán sau", command=self.thanhToanSau).grid(
                column=0, row=self.drow+1, stick=W)
        Button(self.master, text="Thanh toán", command=self.thanhToan).grid(
            column=3, row=self.drow+1, stick=E)
        self.master.mainloop

    def thanhToanSau(self):
        request = messagebox.askquestion(
            "THANH TOÁN SAU", "Ban đồng ý thanh toán sau không?")
        if request:
            Label(self.master, text="THANH TOÁN ĐẶT SAU").grid(
                column=0, columnspan=4, row=self.drow+2)
            self.gioiHan = self.ve[0].chuyenDate()
            self.soNgay = IntVar()
            loi_canh_bao = "Ban chỉ có thể thanh toán sau tối đa {ngay} ngày".format(
                ngay=self.gioiHan)
            Label(self.master, text=loi_canh_bao).grid(
                column=1, columnspan=3, row=self.drow+3)
            Spinbox(self.master, from_=1, to=self.gioiHan, textvariable=self.soNgay).grid(
                column=1, columnspan=2, row=self.drow+4)
            Button(self.master, text="Chấp nhận", command=self.chapNhanTTS).grid(
                column=3, row=self.drow+5, sticky=E)

    def thanhToan(self):
        request = messagebox.askquestion(
            "THANH TOÁN VÉ", "Ban đồng ý thanh toán vé không?")
        if request:
            for i in self.ve:
                i.themKH(self.kh)
            try:
                del(self.object.maVeDSC)
            except:
                pass
            self.master.destroy()

    def chapNhanTTS(self):
        if self.soNgay.get() <= 0 and self.soNgay.get() >= self.gioiHan:
            Label(self.master, text="Chọn lại số ngày").grid(
                column=0, columnspan=3, row=self.drow+5)
        else:
            for i in self.ve:
                i.thanhToanSau(self.soNgay.get(), self.kh)
            try:
                del(self.object.maVeDSC)
            except:
                pass
            self.master.destroy()


App(Tk())
