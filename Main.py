from tkinter import *
from tkinter import ttk
from datetime import datetime
from db import *
# import threading

class App(Frame):
    def __init__(self,master):
        self.master=master
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
        self.ngay= IntVar()
        self.thang =IntVar()
        self.nam = IntVar()
        self.ngay.set(self.ngay_dat_ve.day)
        self.thang.set(self.ngay_dat_ve.month)
        self.nam.set(self.ngay_dat_ve.year)
        self.line_dv= []
        self.trangThai = [None,None,None]
        self.con,self.cur= connect_DB('dac_ve_tau.db')
        self.giaTriGaDen=StringVar()
        self.giaTriGaDi=StringVar()
        self.display()

    def display(self):
        self.master.minsize( width = 600, height = 400)
        self.master.maxsize( width = 600, height = 400)
        self.master.resizable(1,1)
        Button(self.master, text = "Dac ve tau",command=self.dacVeTau,height=3,width=13).place(relx=0,rely=0)
        Button(self.master, text = "Thanh Toan",command=self.thanhToan,width=15,height=3).place(relx=0.33,rely=0)
        Button(self.master, text = "Tim kiem ve", command=self.timKiem).place(relx=0.66,rely=0)
        self.can=Canvas(self.master,bg='MediumPurple1',width=600,height=345,highlightbackground='MediumPurple1',highlightthickness=0)
        self.can.place(x=0,y=55)
        self.master.mainloop()

    def dacVeTau(self):
        if(self.trangThai[0]==None):
            self.kiemTraTrangThai(0)
            self.tenGa=select_Ga(self.cur).fetchall()
            tenGa=[]
            for i in self.tenGa:    
                tenGa.append(i[1])
            self.tenGa.append(('Chọn','Chọn'))
            tenGa.append('chọn')
            self.giaTriGaDen.set('chọn')
            self.giaTriGaDi.set('chọn')
            self.trangThai[0]=1
            for a in range(0,2):
                self.label_dv.append([])
                self.cbb_dv.append([])
                self.button_dv.append([])
                self.line_dv.append([])
            for a in range(0,3):
                self.spinbox.append([])# spinbox [0]:day, [1]:month, [2]:year
            self.title_dv = Label(self.can,text="Dat ve tau",background='MediumPurple1')
            self.label_dv[0]= Label(self.can,text="Ga den",background='MediumPurple1')
            self.label_dv[1]= Label(self.can,text="Ga di",background='MediumPurple1')
            self.spinbox[0] =  Spinbox(self.can,from_=1,to_=31,width=2,textvariable=self.ngay)
            self.spinbox[1] =  Spinbox(self.can,from_=1,to_=12,width=2,textvariable=self.thang,command=self.thietLapGioiHanNgay)
            self.spinbox[2] = Spinbox(self.can,from_=2015,to_=2030,width=8,textvariable=self.nam,command=self.thietLapGioiHanNgay)
            self.button_dv[0]=Button(self.can,text="Tim Kiem",command=self.timVe)
            self.button_dv[1]=Button(self.can,text="Quay lai",command=self.quayLai_dv)
            self.cbb_dv[0]=ttk.Combobox(self.can,width=17,textvariable=self.giaTriGaDen,values=tenGa)
            self.cbb_dv[1]=ttk.Combobox(self.can,width=17,textvariable=self.giaTriGaDi,values=tenGa)
            self.label_dv[0].place(relx=0.1,rely=0.15)
            self.label_dv[1].place(relx=0.1,rely=0.25)
            self.cbb_dv[0].place(relx=0.2,rely=0.15)
            self.cbb_dv[1].place(relx=0.2,rely=0.25)
            self.spinbox[0].place(relx=0.2,rely=0.34)
            self.spinbox[1].place(relx=0.25,rely=0.34)
            self.spinbox[2].place(relx=0.3,rely=0.34)
            self.button_dv[0].place(relx=0.3,rely=0.42)
            self.button_dv[1].place(relx=0.2,rely=0.42)
            self.title_dv.place(relx=0.175,rely=0.065)
            self.line_dv[0] = self.can.create_line(-10,180,250,180)
            self.line_dv[1] = self.can.create_line(250,-3,250,180)
        elif(self.trangThai[0]==0):
            self.kiemTraTrangThai(0)
            self.trangThai[0]=1
            self.hienThiDacVeTau()
        else :
            pass

    def thanhToan(self):
        if(self.trangThai[1]== None):
            self.kiemTraTrangThai(1)
            self.trangThai[1]=1
            self.title_tt = Label(self.can,text="Thanh toan ve tau",background='MediumPurple1')
            self.label_tt = Label(self.can,text="Ma dat truoc",background='MediumPurple1')
            self.entry_tt = Entry(self.can)
            self.button_tt = Button(self.can,text="Tim kiem")
            self.title_tt.place(relx=0.125,rely=0.065)
            self.label_tt.place(relx=0.05,rely=0.2)
            self.entry_tt.place(relx=0.175,rely=0.2)
            self.button_tt.place(relx=0.3,rely=0.4)
        elif(self.trangThai[1]==0):
            self.kiemTraTrangThai(1)    
            self.trangThai[1]=1
            self.hienThiThanhToan()
        else:
            pass


    def timKiem(self):
        if(self.trangThai[2]==None):
            self.kiemTraTrangThai(2)
            self.trangThai[2]=1
            self.title_tk = Label(self.can,text="Tim kiem ve tau",background='MediumPurple1')
            self.label_tk = Label(self.can,text="Ma ve tau",background='MediumPurple1')
            self.entry_tk = Entry(self.can)
            self.button_tk = Button(self.can,text="Tim kiem")
            self.title_tk.place(relx=0.125,rely=0.065)
            self.label_tk.place(relx=0.05,rely=0.2)
            self.entry_tk.place(relx=0.175,rely=0.2)
            self.button_tk.place(relx=0.3,rely=0.4)
        elif(self.trangThai[2]==0):
            self.kiemTraTrangThai(2)
            self.trangThai[2]=1
        else:
            pass



# Line [2,....,n] la Line cua tim ve

    def timVe(self):
        ngayThangNam = str(self.nam.get())+"-"+str(self.thang.get())+"-"+str(self.ngay.get())
        # print(ngayThangNam)
        # print(self.tenGa[self.cbb_dv[0].current()][0])
        # print(self.tenGa[self.cbb_dv[0].current()][0])
        # self.ket_qua = select_CD(self.cur,ngayThangNam,self.tenGa[self.cbb_dv[0].current()][0],self.tenGa[self.cbb_dv[1].current()][0])
        self.ket_qua = select_CD(self.cur,"2021-5-12",self.tenGa[self.cbb_dv[0].current()][0],self.tenGa[self.cbb_dv[1].current()][0])
        if(self.ket_qua):
            self.ket_qua=self.ket_qua.fetchall()
        self.label_stt=[]
        self.label_maSo=[]
        self.label_gaDi=[]
        self.label_gaDen=[]
        self.label_ngayDi=[]
        self.radbu_timVe=[]
        self.giaTri_radbu=[]
        if(self.title_tv == None):
            '''
            tao 1 luong xu ly du lieu
            '''
            self.line_danhSachVe=[]
            self.title_tv = Label(self.can,text='Danh sach dat ve',background='thistle1')
            for i in range(10):
                self.line_dv.append([])
            for i in range(6):
                self.button_tv.append([])
            self.line_dv[2] = self.can.create_line(250,180,600,180)
            self.line_dv[3] = self.can.create_line(250,45,600,45)
            self.line_dv[4] = self.can.create_line(250,70,600,70)
            self.button_tv[0] = Button(self.can,text="Stt",height=1,width=3)
            self.button_tv[1] = Button(self.can,text="Mã số",height=1,width=8)
            self.button_tv[2] = Button(self.can,text="Ga đi",height=1,width=8)
            self.button_tv[3] = Button(self.can,text="Ga đến",height=1,width=8)
            self.button_tv[4] = Button(self.can,text="Ngay đi",height=1,width=8)
            self.button_tv[5] = Button(self.can,height=1,width=7)
            self.button_next = Button(self.can,text='Next')
            self.button_back = Button(self.can,text='Back')
            self.can_tv=Canvas(self.can,height=110,width=350,highlightthickness=0)
            """
            ,bg='MediumPurple1',highlightbackground='MediumPurple1'
            """
            self.themDanhSachVe()
            self.title_tv.place(relx=0.6,rely=0.065)
            self.button_tv[0].place(x=250,y=45)
            self.button_tv[1].place(x=280,y=45)
            self.button_tv[2].place(x=345,y=45)
            self.button_tv[3].place(x=410,y=45)
            self.button_tv[4].place(x=475,y=45)
            self.button_tv[5].place(x=540,y=45)
            self.can_tv.place(x=251,y=70)
        elif(self.title_tv.grid_info()=={}):
            self.title_tv.place(relx=0.6,rely=0.065)
            self.line_dv[2] = self.can.create_line(250,180,600,180)
            self.line_dv[3] = self.can.create_line(250,45,600,45)
            self.line_dv[4] = self.can.create_line(250,70,600,70)
            self.button_tv[0].place(x=250,y=45)
            self.button_tv[1].place(x=280,y=45)
            self.button_tv[2].place(x=345,y=45)
            self.button_tv[3].place(x=410,y=45)
            self.button_tv[4].place(x=475,y=45)
            self.button_tv[5].place(x=540,y=45)

    def quayLai_dv(self):
        self.title_dv.place_forget()
        print(self.title_dv.place_info())

    def kiemTraTrangThai(self,trangThai):
        if(self.trangThai[trangThai]==1):
            return
        for i in range(len(self.trangThai)):
            if(self.trangThai[i]==1):
                self.trangThai[i]=0
                if(i==0):
                    self.title_dv.place_forget()
                    for i in self.label_dv:
                        i.place_forget()
                    for i in self.cbb_dv:
                        i.place_forget()
                    for i in self.spinbox:
                        i.place_forget()
                    for i in self.button_dv:
                        i.place_forget()
                    for i in self.line_dv:
                        self.can.delete(i)
                    if(self.title_tv==None):
                        pass
                    elif(self.title_tv.place_info()!={}):
                        self.title_tv.place_forget()
                        for i in self.label_dv:
                            i.place_forget() 
                        for i in self.button_tv:
                            i.place_forget()
                        self.can_tv.place_forget()
                elif(i==1):
                    self.title_tt.place_forget()
                    self.label_tt.place_forget()
                    self.entry_tt.place_forget()
                    self.button_tt.place_forget()
                elif(i==2):
                    self.title_tk.place_forget()
                    self.label_tk.place_forget()
                    self.entry_tk.place_forget()
                    self.button_tk.place_forget()
        return

    def hienThiDacVeTau(self):
        self.label_dv[0].place(relx=0.1,rely=0.15)
        self.label_dv[1].place(relx=0.1,rely=0.25)
        self.cbb_dv[0].place(relx=0.2,rely=0.15)
        self.cbb_dv[1].place(relx=0.2,rely=0.25)
        self.spinbox[0].place(relx=0.2,rely=0.34)
        self.spinbox[1].place(relx=0.25,rely=0.34)
        self.spinbox[2].place(relx=0.3,rely=0.34)
        self.button_dv[0].place(relx=0.3,rely=0.42)
        self.button_dv[1].place(relx=0.2,rely=0.42)
        self.title_dv.place(relx=0.175,rely=0.065)
        self.line_dv[0] = self.can.create_line(-10,180,250,180)
        self.line_dv[1] = self.can.create_line(250,-3,250,180)

    def hienThiThanhToan(self):
        self.title_tt.place(relx=0.125,rely=0.065)
        self.label_tt.place(relx=0.05,rely=0.2)
        self.entry_tt.place(relx=0.175,rely=0.2)
        self.button_tt.place(relx=0.3,rely=0.4)

    def hienThiTimKiemVe(self):
        self.title_tk.place(relx=0.125,rely=0.065)
        self.label_tk.place(relx=0.05,rely=0.2)
        self.entry_tk.place(relx=0.175,rely=0.2)
        self.button_tk.place(relx=0.3,rely=0.4)

    def thietLapGioiHanNgay(self):
        if(self.thang.get() in [2,4,6,9,11]):
            if(self.thang.get()==2):
                if(self.nam.get()%4==0):
                    if(self.ngay.get()>29):
                        self.ngay.set(29)
                    self.spinbox[0].configure(to_=29)
                else:
                    if(self.ngay.get()>28):
                        self.ngay.set(28)
                    self.spinbox[0].configure(to_=28)
            else: 
                if(self.ngay.get()>30):
                    self.ngay.set(30)
                    self.spinbox[0].configure(to_=30)
        else:
            self.spinbox[0].configure(to_=31)
        pass

    def themDanhSachVe(self):
        Y=0
        self.giaTriChon=IntVar()
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
            self.line_danhSachVe[i][0]=self.can_tv.create_line(29,Y,29,Y+27)#stt
            self.line_danhSachVe[i][1]=self.can_tv.create_line(93,Y,93,Y+27)#maSo
            self.line_danhSachVe[i][2]=self.can_tv.create_line(158,Y,158,Y+30)#gaDi
            self.line_danhSachVe[i][3]=self.can_tv.create_line(223,Y,223,Y+30)#gaDen
            self.line_danhSachVe[i][4]=self.can_tv.create_line(288,Y,288,Y+30)#ngayDi
            self.line_danhSachVe[i][5]=self.can_tv.create_line(347,Y,347,Y+30)#Button
            self.line_danhSachVe[i][6]=self.can_tv.create_line(0,Y+30,347,Y+30)
            self.label_stt[i] = Label(self.can_tv,text=str(i+1),highlightthickness=0)
            self.label_stt[i].place(x=7,y=0+Y+3)
            self.label_maSo[i] = Label(self.can_tv,text=self.ket_qua[i][0],highlightthickness=0,width=8)
            self.label_maSo[i].place(x=31,y=0+Y+3)
            self.label_gaDi[i] = Label(self.can_tv,text= self.ket_qua[i][1],highlightthickness=0,width=8)
            self.label_gaDi[i].place(x=95,y=0+Y+3)
            self.label_gaDen[i] = Label(self.can_tv,text= self.ket_qua[i][2],highlightthickness=0,width=8)
            self.label_gaDen[i].place(x=160,y=0+Y+3)
            self.label_ngayDi[i] = Label(self.can_tv,text=self.ket_qua[0][3],highlightthickness=0,width=8)
            self.label_ngayDi[i].place(x=225,y=0+Y+3)
            self.giaTri_radbu[i]=i
            self.radbu_timVe[i] = Radiobutton(self.can_tv,value =self.giaTri_radbu[i],variable=self.giaTriChon,command=self.onClick,highlightthickness=0)
            self.radbu_timVe[i].place(x=305,y=0+Y+3)
            Y+=30
    def onClick(self):
        print(self.giaTriChon.get())
        
App(Tk())