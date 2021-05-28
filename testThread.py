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
        self.danhSachKhach = []
        self.ngaySinh =  []
        demRow=1
        self.title.grid_forget()
        self.title["text"]= "Danh Sach khach hang dat truoc:"
        self.title.grid(column=0,columnspan=6,row=0)
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
                self.danhSachKhach.append(True)
                chuoi = "Khach hang thu " + str(self.demPhan2+1)
                tam=Label(self.master,text=chuoi)
                tam.grid(column=0,columnspan=3,row=demRow)
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
                self.ngaySinh.append(ngaySinh)
                tam=Label(self.master,text=ngaySinh)
                tam.grid(column=5,row=demRow)
                self.labelPhan2.append(tam)
                demRow+=1
                tam=Label(self.master,text="Ve")
                tam.grid(column=0,row=demRow)
                self.labelPhan2.append(tam)
                try:
                    tam=Label(self.master,text=self.veDaChon[self.demPhan2][0])
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
                tam
                self.labelPhan2.append(tam)
                self.demPhan2+=1
                demRow+=1
        tam=Button(self.master,text="Xác Nhận",command=self.xacNhanDV)
        tam.grid(column=5,row=demRow)
        self.btnPhan2.append(tam)
        tam=Button(self.master,text="Quay lại")
        tam.grid(column=0,row =demRow)
        self.btnPhan2.append(tam)

    def thanhToan(self):
        self.loadTrang2()
        self.labelPhan2 = []
        self.btnPhan2 = []
        self.demPhan2=0
        self.danhSachKhach = []
        self.ngaySinh =  []
        demRow=1
        self.title.grid_forget()
        self.title["text"]= "Danh Sach khach hang dat truoc:"
        self.title.grid(column=0,columnspan=6,row=0)
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
                self.danhSachKhach.append(True)
                chuoi = "Khach hang thu " + str(self.demPhan2+1)
                tam=Label(self.master,text=chuoi)
                tam.grid(column=0,columnspan=3,row=demRow)
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
                self.ngaySinh.append(ngaySinh)
                tam=Label(self.master,text=ngaySinh)
                tam.grid(column=5,row=demRow)
                self.labelPhan2.append(tam)
                demRow+=1
                tam=Label(self.master,text="Ve")
                tam.grid(column=0,row=demRow)
                self.labelPhan2.append(tam)
                try:
                    tam=Label(self.master,text=self.veDaChon[self.demPhan2][0])
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
                tam
                self.labelPhan2.append(tam)
                self.demPhan2+=1
                demRow+=1
                tam=Button(self.master,text="Xác Nhận",command=self.xacNhanTT)
                tam.grid(column=5,row=demRow)
                self.btnPhan2.append(tam)
                tam=Button(self.master,text="Quay lại")
                tam.grid(column=0,row =demRow)
                self.btnPhan2.append(tam)
                break


    def loadTrang2(self):
        for i in self.labelGT:
            i.grid_forget()
        for i in  self.entry:
            i.grid_forget()
        for i in self.cbb:
            i.grid_forget()
        for i in self.btn:
            i.grid_forget()

    def xacNhanDV(self):
        for i in self.labelPhan2:
            i.grid_forget()
        for i in self.btnPhan2:
            i.grid_forget()
        self.title.grid_forget()
        self.LabelPhan3=[]
        self.title['text']="THÔNG TIN VÉ ĐẶT TRƯỚC"
        self.title.grid(column=0,columnspan=2,row=0)
        self.demPhan3=0
        self.demTrue=0
        self.maKH=[]
        dem = 0
        demTrue=0
        self.thongTinVe=[]
        for i in self.danhSachKhach:
            if(i==True):
                maKH=Insert_KH(cur,con,self.valueKH[dem][0].get(),self.valueKH[dem][1].get(),self.ngaySinh[demTrue])
                self.maKH.append(maKH)
                demTrue+=1
            dem+=1
        for i in self.danhSachKhach:
            if(i== True):
                try:
                    thongTinVe=Select_Ve_maVe(cur,self.veDaChon[self.demPhan3][0])
                except:
                    thongTinVe= Select_Ve_maVe(cur,self.veDaChon[0])
                self.thongTinVe.append(thongTinVe)
                    #mave, maCD,gaXuatPhat,gaDen,maCho,maToa,maTau,TrangThai,Gia
                    #ngaydat,ngayhetHan
                tamTTMV=Label(self.master,text="Mã Vé:")
                tamTTMV.grid(column=0,row=1,sticky=W)
                tamVAMV=Label(self.master,text=thongTinVe[0])
                tamVAMV.grid(column=1,row=1,sticky=W)
                tamTTMCD=Label(self.master,text="Mã Chuyến Đi:")
                tamTTMCD.grid(column=0,row=2,sticky=W)
                tamVAMCD=Label(self.master,text=thongTinVe[1])
                tamVAMCD.grid(column=1,row=2,sticky=W)
                tamTTGXP=Label(self.master,text="Ga xuất phát:")
                tamTTGXP.grid(column=0,row=3,sticky=W)
                tamVAGXP=Label(self.master,text=thongTinVe[2])
                tamVAGXP.grid(column=1,row=3,sticky=W)
                tamTTGD=Label(self.master,text="Ga đến:")
                tamTTGD.grid(column=0,row=4,sticky=W)
                tamVAGD=Label(self.master,text=thongTinVe[3])
                tamVAGD.grid(column=1,row=4,sticky=W)
                tamTTND=Label(self.master,text="Ngày ĐI:")
                tamTTND.grid(column=0,row=5,sticky=W)
                tamVAND=Label(self.master,text=thongTinVe[4])
                tamVAND.grid(column=1,row=5,sticky=W)
                tamTTMCD=Label(self.master,text="Mã Chỗ ngồi:")
                tamTTMCD.grid(column=0,row=6,sticky=W)
                tamVACD=Label(self.master,text=thongTinVe[5])
                tamVACD.grid(column=1,row=6,sticky=W)
                tamTTMToa=Label(self.master,text="Mã Toa:")
                tamTTMToa.grid(column=0,row=7,sticky=W)
                tamVAMToa=Label(self.master,text=thongTinVe[6])
                tamVAMToa.grid(column=1,row=7,sticky=W)
                tamTTMTau=Label(self.master,text="Mã Tàu:")
                tamTTMTau.grid(column=0,row=8,sticky=W)
                tamVAMTau=Label(self.master,text=thongTinVe[7])
                tamVAMTau.grid(column=1,row=8,sticky=W)
                tamTTG=Label(self.master,text="Gia: ")
                tamTTG.grid(column=0,row=9,sticky=W)
                tamVAG=Label(self.master,text=thongTinVe[8])
                tamVAG.grid(column=1,row=9,sticky=W)
                tamGTKH=Label(self.master,text="THÔNG TIN KHÁCH HÀNG")
                tamGTKH.grid(column=0,columnspan=2,row=10,sticky=W)
                tamTTmaKH=Label(self.master,text="Mã khách hàng:")
                tamTTmaKH.grid(column=0,row=11,sticky=W)
                tamVAmaKH=Label(self.master,text=self.maKH[self.demTrue])
                tamVAmaKH.grid(column=1,row=11,sticky=W)
                tamTTmaKH=Label(self.master,text="Tên Khách hàng:")
                tamTTmaKH.grid(column=0,row=12,sticky=W)
                tamVAmaKH=Label(self.master,text=self.valueKH[self.demPhan3][0].get())
                tamVAmaKH.grid(column=1,row=12,sticky=W)
                tamTTmaKH=Label(self.master,text="CMND:")
                tamTTmaKH.grid(column=0,row=13,sticky=W)
                tamVAmaKH=Label(self.master,text=self.valueKH[self.demPhan3][1].get())
                tamVAmaKH.grid(column=1,row=13,sticky=W)
                tamTTmaKH=Label(self.master,text="Ngày Sinh:")
                tamTTmaKH.grid(column=0,row=14,sticky=W)
                tamVAmaKH=Label(self.master,text=self.ngaySinh[self.demTrue])
                tamVAmaKH.grid(column=1,row=14,sticky=W)
                self.demTrue+=1
            self.demPhan3+=1
            Button(self.master,text="trang tiếp",command=self.trangTiepDV).grid(column=1,row=15)
            Button(self.master,text="trang trước",command=self.trangTruocDV).grid(column=0,row=15)

    def quayLai(self):
        pass

    def trangTiepDV(self):
        if(self.demTrue < len(self.ngaySinh)):
            pass

    def trangTruocDV(self):
        pass

    def xacNhanTT(self):
        for i in self.labelPhan2:
            i.grid_forget()
        for i in self.btnPhan2:
            i.grid_forget()
        self.title.grid_forget()
        self.LabelPhan3=[]
        self.title['text']="THÔNG TIN VÉ THANH TOÁN"
        self.title.grid(column=0,columnspan=2,row=0)
        self.demPhan3=0
        self.demTrue=0
        self.maKH=[]
        dem = 0
        demTrue=0
        self.thongTinVe=[]
        for i in self.danhSachKhach:
            if(i==True):
                maKH=Insert_KH(cur,con,self.valueKH[dem][0].get(),self.valueKH[dem][1].get(),self.ngaySinh[demTrue])
                self.maKH.append(maKH)
                demTrue+=1
            dem+=1
        for i in self.danhSachKhach:
            if(i== True):
                try:
                    thongTinVe=Select_Ve_maVe(cur,self.veDaChon[self.demPhan3][0])
                except:
                    thongTinVe= Select_Ve_maVe(cur,self.veDaChon[0])
                self.thongTinVe.append(thongTinVe)
                    #mave, maCD,gaXuatPhat,gaDen,maCho,maToa,maTau,TrangThai,Gia
                    #ngaydat,ngayhetHan
                tamTTMV=Label(self.master,text="Mã Vé:")
                tamTTMV.grid(column=0,row=1,sticky=W)
                self.LabelPhan3.append(tamTTMV) #0
                tamVAMV=Label(self.master,text=thongTinVe[0])
                tamVAMV.grid(column=1,row=1,sticky=W)
                self.LabelPhan3.append(tamVAMV) #1
                tamTTMCD=Label(self.master,text="Mã Chuyến Đi:")
                tamTTMCD.grid(column=0,row=2,sticky=W)
                self.LabelPhan3.append(tamTTMCD)#2
                tamVAMCD=Label(self.master,text=thongTinVe[1])
                tamVAMCD.grid(column=1,row=2,sticky=W)
                self.LabelPhan3.append(tamVAMCD)#3
                tamTTGXP=Label(self.master,text="Ga xuất phát:")
                tamTTGXP.grid(column=0,row=3,sticky=W)
                self.LabelPhan3.append(tamTTGXP)#4
                tamVAGXP=Label(self.master,text=thongTinVe[2])
                tamVAGXP.grid(column=1,row=3,sticky=W)
                self.LabelPhan3.append(tamVAGXP)#5
                tamTTGD=Label(self.master,text="Ga đến:")
                tamTTGD.grid(column=0,row=4,sticky=W)
                self.LabelPhan3.append(tamTTGD)#6
                tamVAGD=Label(self.master,text=thongTinVe[3])
                tamVAGD.grid(column=1,row=4,sticky=W)
                self.LabelPhan3.append(tamVAGD)#7
                tamTTND=Label(self.master,text="Ngày ĐI:")
                tamTTND.grid(column=0,row=5,sticky=W)
                self.LabelPhan3.append(tamTTND)#8
                tamVAND=Label(self.master,text=thongTinVe[4])
                tamVAND.grid(column=1,row=5,sticky=W)
                self.LabelPhan3.append(tamVAND)#9
                tamTTMCD=Label(self.master,text="Mã Chỗ ngồi:")
                tamTTMCD.grid(column=0,row=6,sticky=W)
                self.LabelPhan3.append(tamTTMCD)#10
                tamVACD=Label(self.master,text=thongTinVe[5])
                tamVACD.grid(column=1,row=6,sticky=W)
                self.LabelPhan3.append(tamTTMCD)#11
                tamTTMToa=Label(self.master,text="Mã Toa:")
                tamTTMToa.grid(column=0,row=7,sticky=W)
                self.LabelPhan3.append(tamTTMToa)#12
                tamVAMToa=Label(self.master,text=thongTinVe[6])
                tamVAMToa.grid(column=1,row=7,sticky=W)
                self.LabelPhan3.append(tamVAMToa)#13
                tamTTMTau=Label(self.master,text="Mã Tàu:")
                tamTTMTau.grid(column=0,row=8,sticky=W)
                self.LabelPhan3.append(tamTTMTau)#14
                tamVAMTau=Label(self.master,text=thongTinVe[7])
                tamVAMTau.grid(column=1,row=8,sticky=W)
                self.LabelPhan3.append(tamVAMTau)#15
                tamTTG=Label(self.master,text="Gia: ")
                tamTTG.grid(column=0,row=9,sticky=W)
                self.LabelPhan3.append(tamTTG)#16
                tamVAG=Label(self.master,text=thongTinVe[8])
                tamVAG.grid(column=1,row=9,sticky=W)
                self.LabelPhan3.append(tamVAG)#17
                tamGTKH=Label(self.master,text="THÔNG TIN KHÁCH HÀNG")
                tamGTKH.grid(column=0,columnspan=2,row=10,sticky=W)
                self.LabelPhan3.append(tamGTKH)#18
                tamTTmaKH=Label(self.master,text="Mã khách hàng:")
                tamTTmaKH.grid(column=0,row=11,sticky=W)
                self.LabelPhan3.append(tamTTmaKH)#19
                tamVAmaKH=Label(self.master,text=self.maKH[self.demTrue])
                tamVAmaKH.grid(column=1,row=11,sticky=W)
                self.LabelPhan3.append(tamVAmaKH)#20
                tamTTmaKH=Label(self.master,text="Tên Khách hàng:")
                tamTTmaKH.grid(column=0,row=12,sticky=W)
                self.LabelPhan3.append(tamTTmaKH)#21
                tamVAmaKH=Label(self.master,text=self.valueKH[self.demPhan3][0].get())
                tamVAmaKH.grid(column=1,row=12,sticky=W)
                self.LabelPhan3.append(tamVAmaKH)#22
                tamTTmaKH=Label(self.master,text="CMND:")
                tamTTmaKH.grid(column=0,row=13,sticky=W)
                self.LabelPhan3.append(tamTTmaKH)#23
                tamVAmaKH=Label(self.master,text=self.valueKH[self.demPhan3][1].get())
                tamVAmaKH.grid(column=1,row=13,sticky=W)
                self.LabelPhan3.append(tamVAmaKH)#24
                tamTTmaKH=Label(self.master,text="Ngày Sinh:")
                tamTTmaKH.grid(column=0,row=14,sticky=W)
                self.LabelPhan3.append(tamTTmaKH)#25
                tamVAmaKH=Label(self.master,text=self.ngaySinh[self.demTrue])
                tamVAmaKH.grid(column=1,row=14,sticky=W)
                self.LabelPhan3.append(tamVAmaKH)#26
                self.demTrue+=1
            self.demPhan3+=1
            Button(self.master,text="trang tiếp",command=self.trangTiepTT).grid(column=1,row=15)
            Button(self.master,text="trang trước",command=self.trangTruocTT).grid(column=0,row=15)

    def trangTiepTT(self):
        pass

    def trangTruocTT(self):
        if(self.demTrue < len(self.ngaySinh)):
            for i in self.danhSachKhach:
                pass