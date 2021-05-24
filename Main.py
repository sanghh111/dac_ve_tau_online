from re import A, L
from tkinter import * 
from tkinter import ttk
from datetime import datetime
from typing import List, NewType
from db import *
from tkinter.constants import DISABLED, NORMAL
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
        # self.master.bind('<Motion>',self.location)
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

    def timVe(self):
        ngayThangNam = str(self.nam.get())+"-"+str(self.thang.get())+"-"+str(self.ngay.get())
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
        self.thongTinVe = Select_Ve(self.cur,self.ket_qua[self.giaTriChon.get()][0])
        try:
            self.trangThaiToa
        except:
            self.trangThaiToa=False
        if(self.trangThaiToa):
            self.tatDanhSachDatVe()
        self.loadLaiHienThiTau()
        if(self.thongTinVe!=[]):
            self.viTritoa=0
            self.hienThiToaTau()
        else:
            print("không có")
            pass
    
    def hienThiToaTau(self):
        if(self.viTritoa==0):
            self.btnToaBack=Button(self.can,text="trang trước",highlightthickness=0,command=self.backToa)
            self.btnToaNext=Button(self.can,text="trang tiếp",highlightthickness=0,command=self.nextToa)
            self.btnOk = Button(self.can,text="chấp nhận",highlightthickness=0,command=self.oK)
            self.title_toa=Label(self.can,text="",width=30)
            chuoi=(self.thongTinVe[0][2]+"-"+str(self.thongTinVe[0][4])+"VND")
            self.title_toa['text']=chuoi
            self.btnToaBack.place(x=0,y=252)
            self.btnToaNext.place(x=567,y=252)
            self.title_toa.place(x=200,y=205)
            self.btnOk.place(x=520,y=325)
            hcn1 =self.can.create_rectangle(40,200,560,325)
            hcn2 = self.can.create_rectangle(60,210,540,315)
            try:
                self.line_toa[0]=hcn1
            except:
                self.line_toa.append(hcn1)
            try:
                self.line_toa[1]=hcn2
            except:
                self.line_toa.append(hcn2)
            for i in range(16):
                for j in range(4):
                    dem = i*4+j+1
                    a=Button(self.can,text=dem,bg='blue',highlightthickness=0,width=2)
                    a['command']= self.callBackOnClickChoNgoi(btn=a,dem=dem)
                    a.place(x=75+i*29,y=230+j*20)
                    if(self.thongTinVe[dem-1][3]=="Trống"):
                        try:
                            self.button_ve[dem-1]=a
                        except:
                            self.button_ve.append(a)
                    else:
                        a["state"]=DISABLED
                        a["bg"]= 'red'
                        try:
                            self.button_ve[dem-1]=a
                        except:
                            self.button_ve.append(a)
                line_toa=self.can.create_line(74+i*29,230,74+i*29,310)
                try:
                    self.line_toa[i+2]=line_toa
                except:
                    self.line_toa.append(line_toa)
        elif(self.viTritoa==1):
            self.btnToaBack.place(x=0,y=252)
            self.btnToaNext.place(x=567,y=252)
            self.title_toa.place(x=200,y=205)
            self.btnOk.place(x=520,y=325)
            try:
                self.line_toa[0]=self.can.create_rectangle(40,200,560,325)
                self.line_toa[1]=self.can.create_rectangle(45,210,555,315)
            except:
                self.line_toa.append(self.can.create_rectangle(40,200,560,325))
                self.line_toa.append(self.can.create_rectangle(45,210,555,315)) 
            chuoi=(self.thongTinVe[64][2]+"-"+str(self.thongTinVe[64][4])+"VND")
            self.title_toa['text']=chuoi
            for i in range(20):
                for j in range(4):
                    dem = i*4+j+1
                    a=Button(self.can,text=dem,bg='blue',highlightthickness=0,width=2)
                    a.place(x=53+i*25,y=230+j*20)
                    a['command']= self.callBackOnClickChoNgoi(btn=a,dem=dem+64-1)
                    if(self.thongTinVe[dem-1+64][3]=="Trống"):
                        try:
                            self.button_ve[dem-1+64]=a
                        except:
                            self.button_ve.append(a)
                    else:
                        a["state"]=DISABLED
                        a["bg"]= 'red'
                        try:
                            self.button_ve[dem-1+64]=a
                        except:
                            self.button_ve.append(a)
                line_toa=self.can.create_line(52+i*25,230,52+i*25,310)
                try:
                    self.line_toa[i+2]=line_toa
                except:
                    self.line_toa.append(line_toa)
        elif(self.viTritoa==2):#bien dem cho line
            chuoi=(self.thongTinVe[144][2]+"-"+str(self.thongTinVe[144][4])+"VND")
            self.title_toa['text']=chuoi
            self.btnToaBack.place(x=0,y=252)
            self.btnToaNext.place(x=567,y=252)
            self.title_toa.place(x=200,y=205)
            self.btnOk.place(x=520,y=325)
            try:
                self.line_toa[0]=self.can.create_rectangle(40,200,560,325)
                self.line_toa[1]=self.can.create_rectangle(60,210,540,315)
            except:
                self.line_toa.append(self.can.create_rectangle(40,200,560,325))
                self.line_toa.append(self.can.create_rectangle(60,210,540,315))
            for i in range(11):
                for j in range(2):
                    dem = i*2+j+1
                    a=Button(self.can,text=dem,bg='blue',highlightthickness=0,width=2)
                    a['command']= self.callBackOnClickChoNgoi(btn=a,dem=144+dem-1)
                    a.place(x=63+i*35,y=230+j*40)
                    if(self.thongTinVe[dem-1+144][3]=="Trống"):
                        try:
                            self.button_ve[dem-1]=a
                        except:
                            self.button_ve.append(a)
                    else:
                        a["state"]=DISABLED
                        a["bg"]= 'red'
                        try:
                            self.button_ve[dem-1]=a
                        except:
                            self.button_ve.append(a)
                    line_toa=self.can.create_line(62+i*35,230+j*40,62+i*35,260+j*40)
                    try:
                        self.line_toa[i*2+j+3]=line_toa
                    except:
                        self.line_toa.append(line_toa)
        elif(self.viTritoa==3):#bien dem cho line
            chuoi=(self.thongTinVe[168][2]+"-"+str(self.thongTinVe[172][4])+"VND")
            self.title_toa['text']=chuoi
            self.btnToaBack.place(x=0,y=252)
            self.btnToaNext.place(x=567,y=252)
            self.title_toa.place(x=200,y=205)
            self.btnOk.place(x=520,y=325)
            self.line_toa.append(self.can.create_rectangle(40,200,560,325))
            self.line_toa.append(self.can.create_rectangle(60,210,540,315))
            for i in range(14):
                for j in range(3):
                    dem = i*3+j+1
                    a=Button(self.can,text=dem,bg='blue',highlightthickness=0,width=2)
                    a['command']= self.callBackOnClickChoNgoi(btn=a,dem=172+dem-1)
                    a.place(x=63+i*35,y=230+j*40)
                    print(dem-1+168)
                    if(self.thongTinVe[dem-1+168][3]=="Trống"):
                        try:
                            self.button_ve[dem-1]=a
                        except:
                            self.button_ve.append(a)
                    else:
                        a["state"]=DISABLED
                        a["bg"]= 'red'
                        try:
                            self.button_ve[dem-1]=a
                        except:
                            self.button_ve.append(a)
                    line_toa=self.can.create_line(62+i*35,230+j*40,62+i*35,260+j*40)
                    try:
                        self.line_toa[i+2]=line_toa
                    except:
                        self.line_toa.append(line_toa)

    def location(self,event):
        print(event.x,event.y)

    def nextToa(self):
        if(self.viTritoa<3):
            print("next")
            self.loadLaiHienThiTau()
            self.viTritoa+=1
            self.hienThiToaTau()

    def backToa(self):
        if(self.viTritoa>0):
            self.loadLaiHienThiTau()
            self.viTritoa-=1
            self.hienThiToaTau()

    def loadLaiHienThiTau(self):
        try:
            self.title_toa
        except:
             self.title_toa=None
             self.button_ve =[]
             self.line_toa = []
        if(self.title_toa!=None ):
            self.title_toa.place_forget()
            self.title_toa['text']=""
            self.btnToaBack.place_forget()
            self.btnToaNext.place_forget()
            for i in self.button_ve:
                i.place_forget()
            for i in self.line_toa:
                self.can.delete(i)

    def callBackOnClickChoNgoi(self,**kw):
        def __callback():
            return self.onClickChoNgoi(kw)
        return __callback

    def onClickChoNgoi(self, kw):
        self.trangThaiToa = True
        try :
            self.danhSachVe
        except:
            self.danhSachVeChon=[]
            self.soLgDaChon=0
            self.danhSachVe=None
            self.LabelDanhSachChonVe=[]
        if self.danhSachVe==None:
            self.danhSachVe=DanhSachVe(Toplevel(),object=self)
        else:
            if kw['dem'] in self.danhSachVeChon:
                print("true")
                kw['btn']['bg']='blue'
                index= self.danhSachVeChon.index(kw['dem'])
                self.danhSachVeChon.remove(kw['dem'])
                self.LabelDanhSachChonVe[index].pack_forget()
                self.LabelDanhSachChonVe.remove(self.LabelDanhSachChonVe[index])
                self.danhSachVe.master.update()
                return
        self.danhSachVeChon.append(kw['dem'])
        kw['btn']['bg']='yellow'
        self.soLgDaChon+=1
        a=(Label(self.danhSachVe.master,text=kw['dem']))
        print(kw['dem'])
        a.pack()
        self.danhSachVe.master.update()
        try:
            self.LabelDanhSachChonVe[self.soLgDaChon]=a
        except:
            self.LabelDanhSachChonVe.append(a)

    def nhanTinHieu(self,**kw):
        return kw['object']


    def tatDanhSachDatVe(self):
        self.danhSachVe.master.destroy()
        del(self.danhSachVe)
        self.soLgDaChon=0
        self.danhSachVeChon.clear()
        self.LabelDanhSachChonVe.clear()
        self.danhSachVeChon=[]
        self.LabelDanhSachChonVe=[]
        self.btn=[]
        self.trangThaiToa = False
        # print(self.danhSachVe)
        # self.danhSachVe

    def oK(self):
        danhSachVeChon = []
        for i in self.danhSachVeChon:
            print(i)
            danhSachVeChon.append(self.thongTinVe[i-1])
            print(self.thongTinVe[i])
        uIkhachHang=UInhapThongTin(Toplevel(),object=self)
        uIkhachHang.nhanTTVe(danhSachVeChon)
    


class DanhSachVe(Frame):
    def __init__(self,master,**kw):
        self.master = master
        self.guiTinHieu(kw)
        self.display()

    def display(self):
        Label(self.master,text='DANH SÁCH VÉ CHỌN').pack()
        self.master.mainloop

    def guiTinHieu(self,kw):
        kw['object'].nhanTinHieu(object=self)

    def __del__(self):
        return None


class UInhapThongTin(Frame):
    def __init__(self,master,**kw):
        self.master = master
        self.guiTinHieu(kw)
        self.veDaChon = None
        self.labelGT = []
        self.valueKH = []
        self.entry = []
        self.ngay = []
        self.thang = []
        self.nam = []
        self.cbb = []
        self.btn = []
        for i in range(1,32,1):
            self.ngay.append(i)
        for i in range(1,13,1):
            self.thang.append(i)
        for i in range(1950,2020,1):
            self.nam.append(i)
        self.display()

    def display(self):
        a=Label(self.master)
        a.grid(column=0,row=0)
        self.title=a
        self.master.mainloop

    def guiTinHieu(self,kw):
        kw['object'].nhanTinHieu(object=self)

    def nhanTTVe(self,danhSach):
        self.veDaChon = danhSach
        print(self.veDaChon)
        self.themDisplay()

    def themDisplay(self):
        self.Dem = 0
        self.title['text']=self.veDaChon[self.Dem][0]
        a= Label(self.master,text="TenKH:")
        b= Label(self.master,text="Cmnd:")
        c= Label(self.master,text="NgaySinh")
        a.grid(column=0,row=1)
        b.grid(column=0,row=2)
        c.grid(column=0,row=3)
        self.labelGT.append(a)
        self.labelGT.append(b)
        self.labelGT.append(c)
        self.valueKH.append([StringVar(),StringVar(),IntVar(),IntVar(),IntVar()])
        a= (Entry(self.master,textvariable=self.valueKH[self.Dem][0]))
        a.grid(column=1,row=1)
        b= (Entry(self.master,textvariable=self.valueKH[self.Dem][1]))
        b.grid(column=1,row=2)
        c= ttk.Combobox(self.master,width=2,textvariable=self.valueKH[self.Dem][2],values=self.ngay)
        c.grid(column=2,row=3)
        d= ttk.Combobox(self.master,width=2,textvariable=self.valueKH[self.Dem][3],values=self.thang)
        d.grid(column=3,row=3)
        e= ttk.Combobox(self.master,width=6,textvariable=self.valueKH[self.Dem][4],values=self.nam)
        e.grid(column=4,row=3)
        # if
        #  self.cbb_dv[0]=ttk.Combobox(self.can,width=17,textvariable=self.giaTriGaDen,values=tenGa)
        self.entry.append(a)
        self.entry.append(b)
        self.cbb.append(c)
        self.cbb.append(d)
        self.cbb.append(e)
        self.btn.append(Button(self.master,text="Trang tiếp",command=self.trangTiep))
        self.btn.append(Button(self.master,text="Trang trước",command=self.trangTruoc))
        self.btn.append(Button(self.master,text="Dặt Trước",command= self.datTruoc))
        self.btn.append(Button(self.master,text="Thanh Toán",command=self.thanhToan))
        self.btn[0].grid(column=4,row=4)
        self.btn[1].grid(column=0,row=4)
        self.btn[2].grid(column=2,row=4)
        self.btn[3].grid(column=3,row=4)

    def trangTiep(self):
        if self.Dem+1 != len(self.veDaChon):
            self.Dem+=1
            try:
                self.valueKH[self.Dem]
            except:
                self.valueKH.append([StringVar(),StringVar(),IntVar(),IntVar(),IntVar()])
            self.title['text']=self.veDaChon[self.Dem][0]
            self.entry[0]['textvariable']=self.valueKH[self.Dem][0]
            self.entry[1]['textvariable']=self.valueKH[self.Dem][1]
            self.cbb[0]['textvariable']=self.valueKH[self.Dem][2]
            self.cbb[1]['textvariable']=self.valueKH[self.Dem][3]
            self.cbb[2]['textvariable']=self.valueKH[self.Dem][4]
            
    def trangTruoc(self):
        if self.Dem>0:
            self.Dem-=1
            self.title['text']=self.veDaChon[self.Dem][0]
            self.entry[0]['textvariable']=self.valueKH[self.Dem][0]
            self.entry[1]['textvariable']=self.valueKH[self.Dem][1]
            self.cbb[0]['textvariable']=self.valueKH[self.Dem][2]
            self.cbb[1]['textvariable']=self.valueKH[self.Dem][3]
            self.cbb[2]['textvariable']=self.valueKH[self.Dem][4]

    def datTruoc(self):
        self.loadTrang2()
        self.labelPhan2 = []
        self.btnPhan2 = []
        self.demPhan2=0
        demRow=1
        self.title["text"]= "Danh Sach khach hang dat truoc:"
        for i in self.valueKH:
            trangThai = True
            for j in range(2):
                if(i[j].get()==""):
                    trangThai=False
                    break
            for j in range(3):
                if(i[j+2].get()==0):
                    trangThai=False
                    break
            print(trangThai)
            if(trangThai):
                chuoi = "Khach hang thu " + str(self.demPhan2+1)
                tam=Label(self.master,text=chuoi)
                tam.grid(column=0,row=demRow)
                self.labelPhan2.append(tam)
                demRow+=1
                # dem +=1
                tam=Label(self.master,text="Tên khách hàng")
                tam.grid(column=0,row=demRow)
                self.labelPhan2.append(tam)
                tam=Label(self.master,text=i[0].get())
                tam.grid(column=1,row=demRow)
                self.labelPhan2.append(tam)
                tam=Label(self.master,text="CMND")
                tam.grid(column=2,row=demRow)
                self.labelPhan2.append(tam)
                tam=Label(self.master,text=i[1].get())
                tam.grid(column=3,row=demRow)
                self.labelPhan2.append(tam)
                tam=Label(self.master,text="Ngay sinh")
                tam.grid(column=4,row=demRow)
                self.labelPhan2.append(tam)
                ngaySinh = str(i[4].get())+"-"+str(i[3].get())+"-"+str(i[2].get())
                tam=Label(self.master,text=ngaySinh)
                tam.grid(column=5,row=demRow)
                self.labelPhan2.append(tam)
                demRow+=1
                tam=Label(self.master,text="Ve")
                tam.grid(column=0,row=demRow)
                self.labelPhan2.append(tam)
                try:
                    tam=Label(self.master,text=self.veDaChon[dem][0])
                    tam.grid(column=1,row=demRow)
                except:
                    tam=Label(self.master,text=self.veDaChon[0])
                    tam.grid(column=1,row=demRow)
                self.labelPhan2.append(tam)
                tam=Label(self.master,text="Toa")
                tam.grid(column=2,row=demRow)
                self.labelPhan2.append(tam)
                try:
                    tam=Label(self.master,text=self.veDaChon[self.demPhan2][2])
                    tam.grid(column=3,row=demRow)
                except:
                    tam=Label(self.master,text=self.veDaChon[2])
                    tam.grid(column=3,row=demRow)
                self.labelPhan2.append(tam)
                tam=Label(self.master,text="Gia")
                tam.grid(column=4,row=demRow)
                self.labelPhan2.append(tam)
                try:
                    tam=Label(self.master,text=self.veDaChon[self.demPhan2][4])
                    tam.grid(column=5,row=demRow)
                except:
                    tam=Label(self.master,text=self.veDaChon[4])
                    tam.grid(column=5,row=demRow)
                self.labelPhan2.append(tam)
                self.demPhan2+=1
                demRow+=1
        tam=Button(self.master,text="Xác Nhận",command=self.xacNhan)
        tam.grid(column=5,row=demRow)
        self.btnPhan2.append(tam)
        tam=Button(self.master,text="Quay lại")
        tam.grid(column=0,row =demRow)
        self.btnPhan2.append(tam)

    def thanhToan(self):
        pass

    def loadTrang2(self):
        for i in self.labelGT:
            i.grid_forget()
        for i in  self.entry:
            i.grid_forget()
        for i in self.cbb:
            i.grid_forget()
        for i in self.btn:
            i.grid_forget()

    def xacNhan(self):
        for i in self.labelPhan2:
            i.grid_forget()
        for i in self.btnPhan2:
            i.grid_forget()
        self.title.grid_forget()
        Label(self.master,text="Thong tin ve")
        

    def quayLai(self):
        pass
App(Tk())