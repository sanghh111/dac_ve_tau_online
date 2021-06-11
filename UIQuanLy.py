from datetime import datetime
from tkinter import *
from NhanVien import *
from tkinter import ttk,DISABLED,NORMAL,messagebox
from tk_tools import *
import tkinter.font as TkFont
class DangNhap(Frame):
    def __init__(self, master):
        self.master = master
        self.nv = NhanVien()
        self.value = [StringVar(), StringVar()]
        self.display()

    def display(self):
        Label(self.master, text="ĐĂNG NHẬP").grid(
            column=0, row=0, columnspan=3)
        Label(self.master, text="Tên tài khoản").grid(
            column=0, row=1, sticky=W)
        Label(self.master, text="Mật khẩu").grid(column=0, row=2, sticky=W)
        Entry(self.master, textvariable=self.value[0]).grid(column=1, row=1)
        Entry(self.master, show="*",
              textvariable=self.value[1],).grid(column=1, row=2)
        Button(self.master, text="Đăng nhập", command=self.dangNhap).grid(
            column=2, row=3, sticky=E)
        self.lb_tb = Label(self.master, text="Đăng nhập không thành công")
        self.master.mainloop()

    def dangNhap(self):
        self.trangThai = self.nv.dangNhap(
            self.value[0].get(), self.value[1].get())
        if self.trangThai:
            print("Đăng nhập thành công")
            self.master.destroy()
        else:
            if(self.lb_tb.grid_info() == {}):
                print("Đăng nhập thất bại")
                self.lb_tb.grid(column=0, columnspan=2, row=3)
            else:
                pass

    def __del__(self):
        try:
            self.trangThai
        except:
            self.trangThai = None
        if self.trangThai:
            ChucNang(Tk(), self.nv)

class ChucNang(Frame):
    def __init__(self, master, nv):
        self.master = master
        self.nv = nv
        self.display()

    def display(self):
        #co chuc nang gi 


        helv13 = TkFont.Font(family="Helvetica",size=12)

        nooteBook = ttk.Notebook(self.master)
        nooteBook.pack(anchor=CENTER)

        frame_thongTin = Frame(nooteBook,height=200,width=200)
        frame_thongTin.pack(fill="both",expand="TRUE")

        frame_chucNang = Frame(nooteBook,height=200,width=200)
        frame_chucNang.pack(fill="both",expand="TRUE")

        nooteBook.add(frame_thongTin,text="Thông tin")
        nooteBook.add(frame_chucNang,text="Chức năng")
        
        Label(frame_thongTin,text="Tên",font=helv13).grid(column=0,row=0,sticky=W)
        Label(frame_thongTin,text="Ngày sinh",font=helv13).grid(column=0,row=1,sticky=W)
        Label(frame_thongTin,text="CMND",font=helv13).grid(column=0,row=2,sticky=W)
        Label(frame_thongTin,text="Số điện thoại",font=helv13).grid(column=0,row=3,sticky=W)
        Label(frame_thongTin,text="Chức vụ",font=helv13).grid(column=0,row=4,sticky=W)

        Label(frame_thongTin,font=helv13,text=self.nv.getTenNV()).grid(column=1,row=0,sticky=W)
        Label(frame_thongTin,font=helv13,text=self.nv.getNgaySinh()).grid(column=1,row=1,sticky=W)
        Label(frame_thongTin,font=helv13,text=self.nv.getCMND()).grid(column=1,row=2,sticky=W)
        Label(frame_thongTin,font=helv13,text=self.nv.getSDT()).grid(column=1,row=3,sticky=W)
        Label(frame_thongTin,font=helv13,text=self.nv.getChucVu()).grid(column=1,row=4,sticky=W)
        
        Label(frame_chucNang,text="",width=8).grid(column=0,row=0)
        Label(frame_thongTin,text="",width=8).grid(column=0,row=5)

        Button(frame_chucNang, text="Quản lý tàu",command=self.quanLyTau).grid(row=0,sticky=W,column=1)
        Button(frame_chucNang, text="Quản lý nhà ga",command=self.quanLyNhaGa).grid(row=1,sticky=W,column=1)
        Button(frame_chucNang, text="Quản lý chuyến đi",command=self.quanLyChuyenDi).grid(row=2,sticky=W,column=1)
        Button(frame_chucNang, text="Quản lý toa tàu",command=self.quanLyToaTau).grid(row=3,sticky=W,column=1)
        Button(frame_chucNang, text="Quản lý vé tàu",command=self.quanLyVe).grid(row=4,sticky=W,column=1)
        if self.nv.getChucVu() == "Quản trị viên":
            Button(frame_chucNang, text="Quản lý nhân viên",command=self.quanLyNhanVien).grid(row=5,sticky=W,column=1)
            
        Button(frame_thongTin, text="Đăng xuất",command=self.dangXuat).grid(row=6,column=2,stick=E)
        self.master.geometry("300x200")
        self.master.mainloop()

    def dangXuat(self):
        self.trangThai =  True
        self.master.destroy()
    
    def quanLyTau(self):
        QuanLyTau(Toplevel())

    def quanLyNhaGa(self):
        QuanLyGaTau(Toplevel())

    def quanLyChuyenDi(self):
        QuanLyChuyenDi(Toplevel())

    def quanLyToaTau(self):
        QuanLyToaTau(Toplevel())

    def quanLyVe(self):
        QuanLyVeTau(Toplevel())

    def quanLyNhanVien(self):
        QuanLyNhanVien(Toplevel())


    def __del__(self):
        try:
            self.trangThai
        except:
            self.trangThai = None
        if self.trangThai:
            DangNhap(Tk())

class QuanLyTau(Frame):
    def __init__(self,master):
        self.master = master
        self.value = [StringVar(),StringVar()]
        self.display()

    def display(self):
        Label(self.master,text="QUẢN LÝ NHÀ GA").pack()
        #Create Tree Frame
        self.tree_frame = Frame(self.master)
        self.tree_frame.pack(expand="yes")
        
        #Create Treeview Scrollbar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT,fill= Y)
        
        #Add style
        style = ttk.Style()
        #ping a theme
        style.theme_use('default')

        #configure Treeview
        style.configure("Treeview",
            background='#D3D3D3',
            foreground='black',
            rowheight=25,
            fieldbackground='silver')

        #Change selected color
        style.map('Treeview',
            background=[('selected','red')])
        #Create Treeview
        self.tree = ttk.Treeview(self.tree_frame,
                                yscrollcommand=self.tree_scroll)
        self.tree.pack()

        #Defind Our Column
        self.tree['columns']= ("Mã tàu","Tên tàu")

        #Formate our column
        self.tree.column('#0',width = 0,stretch = NO)
        self.tree.column('Mã tàu',anchor=W,width = 80)
        self.tree.column('Tên tàu',anchor=W,width = 160)
        
        #Create heading
        self.tree.heading("#0",text="")
        self.tree.heading("Mã tàu",text="Mã tàu",anchor=W)
        self.tree.heading("Tên tàu",text="Tên tàu",anchor=W)

        #add Data
        self.Tau = select_tau(cur).fetchall()
        self.iid = 0
        for i in self.Tau:
            self.tree.insert(parent="",index="end",iid=self.iid,values=i)
            self.iid+=1

        #Create Frame Select item
        self.item_frame = Frame(self.master)
        self.item_frame.pack()

        #Label Select item 
        Label(self.item_frame,text="Mã tàu").grid(column=0,row=0)
        Label(self.item_frame,text="Tên tàu").grid(column=1,row=0)

        #Entry select item
        Entry(self.item_frame,textvariable=self.value[0]).grid(column=0,row=1)
        Entry(self.item_frame,textvariable=self.value[1]).grid(column=1,row=1)
        
        self.lb = Label(self.item_frame)
        self.lb.grid(column=0,columnspan=2,row=2)
        Button(self.item_frame,text="Thêm tàu",width=10,command=self.themTau).grid(column=0,columnspan=2,row=3)
        Button(self.item_frame,text="Xóa tàu",width=10,command=self.xoaTau).grid(column=0,columnspan=2,row=4)
        Button(self.item_frame,text="Sửa tàu",width=10,command=self.suaTau).grid(column=0,columnspan=2,row=5)

        #Envent Select Item
        self.tree.bind("<<TreeviewSelect>>",self.select_item)

        #Run Tkinter
        self.master.geometry("500x500")
        self.master.mainloop

    #Chuc nang them tau
    def themTau(self):
        if self.value[0].get() == "" and self.value[1].get() == "":
            pass
        else:
            for i in self.Tau:
                if i[0] == self.value[0].get():
                    self.lb['text'] = "Đã tồn tại mã toa"
                    return
            trang_thai = insert_tau(con,cur,self.value[0].get(),self.value[1].get())
            if trang_thai:
                messagebox.showinfo("THÔNG BÁO","THÊM TÀU THÀNH CÔNG")
                self.Tau.append((self.value[0].get(),self.value[1].get()))
                self.tree.insert(parent="",index="end",iid=self.iid,values=self.Tau[self.iid])
                self.iid+=1
                for i in self.value:
                    i.set("")
                self.lb['text'] = ""
                return
            self.lb['text'] = "Nhập thiếu thuộc tính"

    #su khien lua chon record
    def select_item(self,event):
        #focus when select record
        self.selected = self.tree.focus()
        #get value
        values = self.tree.item(self.selected,'values')
        #give entry values by selected
        self.value[0].set(values[0])
        self.value[1].set(values[1])

    #Chuc nang xoa
    def xoaTau(self):
        values = self.tree.item(self.selected,'values')
        cau_hoi = "Bạn có muốn xóa mã tàu "+values[0]+", tên tàu "+values[1]
        trangThai = messagebox.askquestion("THÔNG BÁO",cau_hoi)
        if (trangThai):
            trang_thai = delete_tau(values[0])
            if(trang_thai):
                messagebox.showinfo("THÔNG BÁO","XÓA THÀNH CÔNG")
                self.tree.delete(self.selected)
                self.value[0].set("")
                self.value[1].set("")
            else:
                messagebox.showinfo("THÔNG BÁO","XÓA KHÔNG THÀNH CÔNG")

    #Chuc nang sua
    def suaTau(self):
        values = self.tree.item(self.selected,'values')
        cau_hoi = "Bạn có muốn thay đổi\n"
        ma = False
        ten = False
        if(self.value[0].get() != values[0] and self.value[0].get() != ""):
            ma = True
            cau_hoi += "Mã Tàu: "+values[0]+" --> "+self.value[0].get()
        if(self.value[1].get() != values[1] and self.value[1].get() != ""):
            ten = True
            cau_hoi += "Tên Tàu: "+values[1]+" --> "+self.value[1].get()
        if cau_hoi != "Bạn có muốn thay đổi\n":
            trangThai = messagebox.askquestion("THÔNG BÁO",cau_hoi)
            if ma == True and ten == True:
                trang_Thai = update_tau(values[0],self.value[0].get(),self.value[1].get())
            elif ma == True:
                trang_Thai = update_tau(values[0],self.value[0].get(),None)
            else:
                trang_Thai = update_tau(values[0],None,self.value[1].get())
            if trang_Thai :
                messagebox.showinfo("THÔNG BÁO","THAY ĐỔI THÀNH CÔNG")
                self.tree.item(self.selected,values=(self.value[0].get(),self.value[1].get()))
                self.value[0].set("")
                self.value[1].set("")
            else:
                messagebox.showinfo("THÔNG BÁO","THAY ĐỔI KHÔNG THÀNH CÔNG")

class QuanLyGaTau(Frame):
    def __init__(self,master):
        self.master = master
        self.value = [StringVar(),StringVar(),StringVar(),IntVar(),IntVar()]
        self.display()

    def display(self):
        Label(self.master,text="QUẢN LÝ NHÀ GA").pack()
        #Create Tree Frame
        self.tree_frame = LabelFrame(self.master,text="View")
        self.tree_frame.pack(expand="yes")
        
        #Create Treeview Scrollbar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT,fill= Y)
        
        #Add style
        style = ttk.Style()
        
        #ping a theme
        style.theme_use('default')

        #configure Treeview
        style.configure("Treeview",
            background='#D3D3D3',
            foreground='black',
            rowheight=25,
            fieldbackground='silver')

        #Change selected color
        style.map('Treeview',
            background=[('selected','red')])
        #Create Treeview
        self.tree = ttk.Treeview(self.tree_frame,
                                yscrollcommand=self.tree_scroll)
        self.tree.pack()

        #Defind Our Column
        self.tree['columns']= ("Mã Ga","Tên Ga","Vị trí","Chiều dài(KM)","Chiều rộng(KM)")

        #Formate our column
        self.tree.column('#0',width = 0,stretch = NO)
        self.tree.column('Mã Ga',anchor=W,width = 40)
        self.tree.column('Tên Ga',anchor=W,width = 120)
        self.tree.column('Vị trí',anchor=W,width = 120)
        self.tree.column('Chiều dài(KM)',anchor=W,width = 80)
        self.tree.column('Chiều rộng(KM)',anchor=W,width = 90)
        
        #Create heading
        self.tree.heading("#0",text="")
        self.tree.heading("Mã Ga",text="Mã Ga",anchor=W)
        self.tree.heading("Tên Ga",text="Tên Ga",anchor=W)
        self.tree.heading("Vị trí",text="Vị trí",anchor=W)
        self.tree.heading("Chiều dài(KM)",text="Chiều dài(KM)",anchor=W)
        self.tree.heading("Chiều rộng(KM)",text="Chiều rộng(KM)",anchor=W)

        #add Data
        self.Ga = select_Ga_all(cur).fetchall()
        self.iid = 0
        for i in self.Ga:
            self.tree.insert(parent="",index="end",iid=self.iid,values=i)
            self.iid+=1

        #Create Frame Select item
        self.item_frame = LabelFrame(self.master,text="Record")
        self.item_frame.pack()

        #Label Select item 
        Label(self.item_frame,text="Mã Ga").grid(column=0,row=0)
        Label(self.item_frame,text="Tên Ga").grid(column=2,row=0)
        Label(self.item_frame,text="Vị trí").grid(column=0,row=1)
        Label(self.item_frame,text="Chiều dài").grid(column=2,row=1)
        Label(self.item_frame,text="Chiều rộng").grid(column=0,row=2)

        #Entry select item
        Entry(self.item_frame,textvariable=self.value[0]).grid(column=1,row=0)
        Entry(self.item_frame,textvariable=self.value[1]).grid(column=3,row=0)
        Entry(self.item_frame,textvariable=self.value[2]).grid(column=1,row=1)
        Entry(self.item_frame,textvariable=self.value[3]).grid(column=3,row=1)
        Entry(self.item_frame,textvariable=self.value[4]).grid(column=1,row=2)
        
        self.lb = Label(self.item_frame)
        self.lb.grid(column=2,columnspan=2,row=2)

        self.frame_chuc_nang = LabelFrame(self.master,text="Commands")
        self.frame_chuc_nang.pack(expand="yes")

        Button(self.frame_chuc_nang,text="Thêm Ga",width=10,command=self.themGa).grid(column=1,row=0)
        Button(self.frame_chuc_nang,text="Xóa Ga",width=10,command=self.xoaGa).grid(column=2,row=0)
        Button(self.frame_chuc_nang,text="Sửa Ga",width=10,command=self.suaGa).grid(column=3,row=0)

        #Envent Select Item
        self.tree.bind("<<TreeviewSelect>>",self.select_item)

        #Run Tkinter
        self.master.geometry("700x500")
        self.master.mainloop

    #Chuc nang them nha Ga
    def themGa(self):
        if (self.value[0].get() == "" 
        and self.value[1].get() == ""
        and self.value[2].get() == ""
        and self.value[3].get() == 0
        and self.value[4].get() == 0):
            pass
        else:
            for i in self.Ga:
                if i[0] == self.value[0].get():
                    self.lb['text'] = "Đã tồn tại mã toa"
                    return
            trang_thai = insert_ga(self.value[0].get(),
                                self.value[1].get(),
                                self.value[2].get(),
                                self.value[3].get(),
                                self.value[4].get())
            if trang_thai:
                messagebox.showinfo("THÔNG BÁO","THÊM GA TÀU THÀNH CÔNG")
                self.Ga.append((self.value[0].get(),
                                self.value[1].get(),
                                self.value[2].get(),
                                self.value[3].get(),
                                self.value[4].get()))
                self.tree.insert(parent="",index="end",iid=self.iid,values=self.Ga[self.iid])
                self.iid+=1
                for i in range(3):
                    self.value[i].set("")
                self.value[3].set(0)
                self.value[4].set(0)
                self.lb['text'] = ""
                return
            self.lb['text'] = "Nhập thiếu thuộc tính"

    #su khien lua chon record
    def select_item(self,event):
        #focus when select record
        self.selected = self.tree.focus()
        #get value
        values = self.tree.item(self.selected,'values')
        #give entry values by selected
        self.value[0].set(values[0])
        self.value[1].set(values[1])
        self.value[2].set(values[2])
        self.value[3].set(values[3])
        self.value[4].set(values[4])

    #Chuc nang xoa
    def xoaGa(self):
        values = self.tree.item(self.selected,'values')
        cau_hoi = "Bạn có muốn xóa mã ga "+values[0]
        trangThai = messagebox.askquestion("THÔNG BÁO",cau_hoi)
        if (trangThai):
            trang_thai = delete_Ga(values[0])
            if(trang_thai):
                messagebox.showinfo("THÔNG BÁO","XÓA THÀNH CÔNG")
                self.tree.delete(self.selected)
                for i in range(3):
                    self.value[i].set("")
                self.value[3].set(0)
                self.value[4].set(0)
            else:
                messagebox.showinfo("THÔNG BÁO","XÓA KHÔNG THÀNH CÔNG")

    def suaGa(self):
        values = self.tree.item(self.selected,'values')
        cau_hoi = "Bạn có muốn thay đổi\n"
        ma = False
        ten = False
        vt = False
        Dai = False
        Rong = False
        if(self.value[0].get() != values[0] and self.value[0].get() != ""):
            ma = True
            cau_hoi += "Mã Tàu: "+values[0]+" --> "+self.value[0].get()+"\n"
        if(self.value[1].get() != values[1] and self.value[1].get() != ""):
            ten = True
            cau_hoi += "Tên Tàu: "+values[1]+" --> "+self.value[1].get()+"\n"
        if(self.value[2].get() != values[2] and self.value[2].get() != ""):
            vt = True
            cau_hoi += "Vị trí: "+values[2]+" --> "+self.value[2].get()+"\n"
        if(str(self.value[3].get()) != values[3] and self.value[3].get() != 0):
            ten = True
            cau_hoi += "Chiều dài: "+values[3]+" --> "+str(self.value[3].get())+"\n"
        if(str(self.value[4].get()) != values[4] and self.value[4].get() != 0):
            vt = True
            cau_hoi += "Chiều rộng: "+values[4]+" --> "+str(self.value[4].get())+"\n"
        if cau_hoi != "Bạn có muốn thay đổi\n":
            trangThai = messagebox.askquestion("THÔNG BÁO",cau_hoi)
            if trangThai != "no":
                trang_Thai = update_ga(values[0],
                                    self.value[0].get(),
                                    self.value[1].get(),
                                    self.value[2].get(),
                                    self.value[3].get(),
                                    self.value[4].get(),)
                if trang_Thai :
                    messagebox.showinfo("THÔNG BÁO","THAY ĐỔI THÀNH CÔNG")
                    self.tree.item(self.selected,values=(self.value[0].get(),
                                                        self.value[1].get(),
                                                        self.value[2].get(),
                                                        self.value[3].get(),
                                                        self.value[4].get()))
                    for i in range(3):
                        self.value[i].set("")
                    self.value[3].set(0)
                    self.value[4].set(0)
                else:
                    messagebox.showinfo("THÔNG BÁO","THAY ĐỔI KHÔNG THÀNH CÔNG")

class QuanLyChuyenDi(Frame):
    def __init__(self,master):
        self.master = master
        self.display()
    
    def display(self):
        Label(self.master , text = "Quản lý chuyến đi").pack()

        #Tree Frame
        tree_Frame = LabelFrame(self.master,text="VIEW")
        tree_Frame.pack()

        sroll_bar = Scrollbar(tree_Frame)
        sroll_bar.pack(side=RIGHT,fill=Y)

        style = ttk.Style()

        #ping a theme
        style.theme_use('default')

        #configure Treeview
        style.configure("Treeview",
            background='#D3D3D3',
            foreground='black',
            rowheight=25,
            fieldbackground='silver')

        #Create tree view
        self.tree = ttk.Treeview(tree_Frame,
                                yscrollcommand=sroll_bar)
        self.tree.pack()

        #Defind column for Treeview
        self.tree['column'] = ("Mã chuyến đi","Mã tàu","Mã ga xuất phát","Mã ga đến","Ngày khởi hành")

        #Create column
        self.tree.column("#0",width=0,stretch=NO)
        self.tree.column("Mã chuyến đi",width=100)
        self.tree.column("Mã tàu",width=100)
        self.tree.column("Mã ga xuất phát",width=120)
        self.tree.column("Mã ga đến",width=120)
        self.tree.column("Ngày khởi hành",width=120)

        self.tree.heading("#0",text="")
        self.tree.heading("Mã chuyến đi",anchor=CENTER,text="Mã chuyến đi")
        self.tree.heading("Mã tàu",text="Mã tàu",anchor=CENTER)
        self.tree.heading("Mã ga xuất phát",text="Mã ga xuất phát",anchor=CENTER)
        self.tree.heading("Mã ga đến",text="Mã ga đến",anchor=CENTER)
        self.tree.heading("Ngày khởi hành",text="Ngày khởi hành",anchor=CENTER)

        self.chuyenDi = select_CD_all()
        self.IID=0
        for i in self.chuyenDi:
            self.tree.insert(parent="",index="end",iid=self.IID,value= i)
            self.IID+=1

        frame_record = LabelFrame(self.master,text="RECORD")
        frame_record.pack()

        Label(frame_record,text="Mã chuyến đi")
        Label(frame_record,text="Mã tàu")
        Label(frame_record,text="Mã ga xuất phát")
        Label(frame_record,text="Mã ga đến")
        Label(frame_record,text="Ngày khỏi hành")
        
        #DATA 6 atribute And data
        self.value = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        Ga=select_Ga(cur).fetchall()
        maTau = select_tau_ma()
        self.maGa = []
        for i in Ga:
            self.maGa.append(i[0])
        self.maTau = []
        for i in maTau:
            self.maTau.append(i[0])


        #create Label
        Label(frame_record , text="Mã Chuyến đi").grid(column=0,stick=W,row=0)
        Label(frame_record, text="Mã tàu").grid(column=0,stick=W,row=1)
        Label(frame_record, text="Mã ga xuất phát").grid(column=0,stick=W,row=2)
        Label(frame_record, text="Mã ga đến").grid(column=0,stick=W,row=3)
        Label(frame_record, text="Ngày khởi hành").grid(column=0,stick=W,row=4)

        #create Entry
        Entry(frame_record,textvariable=self.value[0],width=22).grid(column=1,row=0)
        ttk.Combobox(frame_record,textvariable=self.value[1],values=self.maTau).grid(column=1,row=1)
        ttk.Combobox(frame_record,textvariable=self.value[2],values=self.maGa).grid(column=1,row=2)
        ttk.Combobox(frame_record,textvariable=self.value[3],values=self.maGa).grid(column=1,row=3)
        Entry(frame_record,textvariable=self.value[4],width=22).grid(column=1,row=4)
        
        Label(frame_record,text="",width=18).grid(column=2,row=0)

        self.value[4].set("YY-MM-DD")

        #Defind NGAY THANG NAM
        self.date =None

        #Create Calendar    
        self.calender = Calendar(frame_record,callback=self.on_click_calender,object = self)
        self.calender.grid(column=3,rowspan=5,row=0,sticky=E)

        command_frame = LabelFrame(self.master,text="COMMAND")
        command_frame.pack()

        #Button
        Button(command_frame,text="Thêm chuyến đi",command=self.themChuyenDi).grid(column=0,row=0)
        Label(command_frame,text="",width=22).grid(column=1,row=0)
        Button(command_frame,text="Xoá chuyến đi",command=self.xoaChuyenDi).grid(column=2,row=0)
        Label(command_frame,text="",width=22).grid(column=3,row=0)
        Button(command_frame,text="Sửa chuyến đi",command=self.suaChuyenDi).grid(column=4,row=0)

        #Bind treeview
        self.tree.bind("<<TreeviewSelect>>",self.chon)

        self.master.geometry("600x600")
        self.master.mainloop
    
    def on_click_calender(self):
        ngay = self.calender.getTime()
        self.date = date(year=ngay[0],month=ngay[1],day=ngay[2])
        self.value[4].set(self.date)

    def huyChon(self):
        self.date = None
        self.value[4].set("YY-MM-DD")

    def themChuyenDi(self):
        for i in range (0,4):
            if self.value[i].get() == "":
                messagebox.showerror("LỖI","NHẬP KHÔNG ĐỦ TÍNH THẤT BẠI")
                return
        if self.value[4].get() == ("YY-MM-DD"):
            messagebox.showerror("LỖI","NHẬP KHÔNG ĐỦ TÍNH THẤT BẠI")
            return
        print('self.value[1].get(): ', self.value[1].get())
        print('self.maTau: ', self.maTau)
        print('self.value[1].get() not in self.maTau: ', self.value[1].get() not in self.maTau)
        if self.value[1].get() not in self.maTau:
            messagebox.showerror("LỖI","MÃ TÀU KHÔNG CÓ SẴN")
            return
        if self.value[2].get() not in self.maGa and self.value[3].get() not in self.maGa:
            messagebox.showerror("LỖI","MÃ GA KHÔNG CÓ SẴN")
            return
        if self.value[2].get() == self.value[3].get():
            messagebox.showerror("LỖI","MÃ GA ĐẾN TRÙNG MÃ GA ĐI")
        print("them cd")
        a = insert_CD(self.value[0].get(),
                  self.value[1].get(),
                  self.value[2].get(),
                  self.value[3].get(),
                  self.value[4].get())
        print('a: ', type(a))
        print('a: ', a)
        print('a=="Thieu gia tien ngayBatDau va ngayKetThuc": ', a=="Thieu gia tien ngayBatDau va ngayKetThuc")
        if a == True:
            messagebox.showinfo("THÔNG BÁO","THÊM THÀNH CÔNG")
            self.chuyenDi.append((self.value[0].get(),
                  self.value[1].get(),
                  self.value[2].get(),
                  self.value[3].get(),
                  self.value[4].get()))
            try:
                self.tree.insert("","end",self.IID,value=self.chuyenDi[self.IID])
                self.IID +=1
            except:
                con.rollback()
            con.commit()
        elif(str(a)=="Thieu gia tien ngayBatDau va ngayKetThuc"):
            messagebox.showerror("LỖI","THIẾU GIÁ TIỀN")
            con.rollback()
        elif(str(a)=="TÀU BỊ TRÙNG"):
            messagebox.showerror("LỖI","TÀU VÀO NGÀY "+self.value[4].get()+" BỊ TRÙNG")
            con.rollback()
            self.dinhDangData()
        elif(str(a)=="UNIQUE constraint failed: ChuyenDI.maCD"):
            messagebox.showerror("LỖI","MÃ CHUYẾN ĐI BỊ TRÙNG")
        else :
            messagebox.showinfo("THÔNG BÁO","THÊM KHÔNG THÀNH CÔNG THÀNH CÔNG")
            con.rollback()

    def chon(self,e):
        self.selected= self.tree.focus()
        value = self.tree.item(self.selected,"value")
        self.value[0].set(value[0])
        self.value[1].set(value[1])
        self.value[2].set(value[2])
        self.value[3].set(value[3])
        self.value[4].set(value[4])

    def dinhDangData(self):
        self.value[0].get("")
        self.value[1].get("")
        self.value[2].get("")
        self.value[3].get("")
        self.value[4].set("YY-MM-DD")

    def xoaChuyenDi(self):
        try:
            value = self.tree.item(self.selected,'value')
        except:
            return
        trangThai = delete_CD(value[0])
        if trangThai == True:
            print("Thanh cong")
            messagebox.showinfo("THÔNG BÁO","THÔNG BÁO XÓA THÀNH CÔNG")
            self.tree.delete(self.selected)
            con.commit()
        else:
            messagebox.showerror("THÔNG BÁO","THÔNG BÁO VÉ ĐÃ CÓ NGƯỜI ĐẶT")
            con.rollback()

    def suaChuyenDi(self):
        try:
            value = self.tree.item(self.selected,'value')
        except:
            return
        trang_thai = False
        for i in range(5):
            if(self.value[i].get()!=value[i]):
                trang_thai = True
                break
        if trang_thai:
            trangThai=Update_CD(self.value[0].get(),
                                self.value[1].get(),
                                self.value[2].get(),
                                self.value[3].get(),
                                self.value[4].get(),
                                value[0],
                                value[1],
                                value[4])
            print('trangThai: ', trang_thai)
            if trangThai == True:
                self.tree.item(self.selected,value=(self.value[0].get(),
                                                    self.value[1].get(),
                                                    self.value[2].get(),
                                                    self.value[3].get(),
                                                    self.value[4].get()))
                messagebox.showinfo("THÔNG BÁO","SỬA THÀNH CÔNG")
                con.commit()
            else:
                messagebox.showinfo("Thông báo",str(trangThai))
        else:
            pass

class QuanLyToaTau(Frame):
    def __init__(self,master):
        self.master=master
        self.value = [StringVar(),StringVar(),IntVar(),IntVar(),StringVar(),StringVar()]
        self.chua = [1,1,1,1]
        self.display()

    def display(self):
        Label(self.master,text="QUẢN LÝ TOA TÀU").pack()
        #Create Tree Frame
        self.tree_frame = LabelFrame(self.master,text="View")
        self.tree_frame.pack(expand="yes")
        
        #Create Treeview Scrollbar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT,fill= Y)
        
        #Add style
        style = ttk.Style()
        
        #ping a theme
        style.theme_use('default')

        #configure Treeview
        style.configure("Treeview",
            background='#D3D3D3',
            foreground='black',
            rowheight=25,
            fieldbackground='silver')

        #Change selected color
        style.map('Treeview',
            background=[('selected','red')])
        
        #Create Treeview
        self.tree = ttk.Treeview(self.tree_frame,
                                yscrollcommand=self.tree_scroll)
        self.tree.pack()

        #SET Column for TreeView
        self.tree['column']=("Mã toa","Tên toa","Số chỗ","Giá toa","ngày bắt đầu","ngày kết thúc")

        #Create column
        self.tree.column("#0", width = 10 )
        self.tree.column("Mã toa", anchor=W , width=60)
        self.tree.column("Tên toa", anchor=W, width=120)
        self.tree.column("Số chỗ", anchor=CENTER, width=120)
        self.tree.column("Giá toa", anchor=CENTER, width=120)
        self.tree.column("ngày bắt đầu",anchor=W,width=100)
        self.tree.column("ngày kết thúc",anchor=W,width=100)

        #Set Heading
        self.tree.heading("#0",text="")
        self.tree.heading("Mã toa",text = "Mã toa")
        self.tree.heading("Tên toa",text= "Tên toa")
        self.tree.heading("Số chỗ",text= "Số chỗ")
        self.tree.heading("Giá toa",text= "Giá toa")
        self.tree.heading("ngày bắt đầu",text="ngày bắt đầu")
        self.tree.heading("ngày kết thúc",text="ngày kết thúc")

        #defind new TOA is parent item and IID
        self.parent_Toa = []
        self.IID =0
        
        #Insert treeview item
        self.toa = select_toa_tau(cur)
        self.toa = self.toa.fetchall()
        for i in self.toa:
            self.parent_Toa.append(None)
            self.parent_Toa[self.IID] = self.tree.insert("","end",iid=self.IID,values=i)
            child = select_NKGT(i[0])
            if child :
                count =1
                for j in child:
                    tam = str(self.IID) + "." + str(count)
                    self.chua[self.IID]=count
                    self.tree.insert(self.parent_Toa[self.IID],"end",iid=tam,values=(i[0],
                                                                                    i[1],
                                                                                    i[2],
                                                                                    j[1],
                                                                                    j[2],
                                                                                    j[3]))
                    count +=1
            self.IID += 1

        #frame record
        record =  LabelFrame(self.master,text="RECORD")
        record.pack(expand="yes")

        #Create atrribute for Frame record
        #Mã toa
        Label(record,text="Mã toa").grid(column=0,row=0)
        Entry(record,textvariable=self.value[0]).grid(column=1,row=0)

        #Tên toa
        Label(record,text="Tên toa").grid(column=2,row=0)
        Entry(record,textvariable=self.value[1]).grid(column=3,row=0)

        #Chỗ ngồi
        Label(record,text="Chỗ ngồi").grid(column=4,row=0)
        Entry(record,textvariable=self.value[2]).grid(column=5,row=0)

        #Giá
        Label(record,text="Giá").grid(column=0,row=1)
        Entry(record,textvariable=self.value[3]).grid(column=1,row=1)

        #Ngày bắt đầu
        Label(record,text="Ngày bắt đầu").grid(column=2,row=1)
        Entry(record,textvariable=self.value[4]).grid(column=3,row=1)

        #Ngày kết thúc
        Label(record,text="Ngày kết thúc").grid(column=4,row=1)
        Entry(record,textvariable=self.value[5]).grid(column=5,row=1)
        self.value[4].set("YY-MM-DD")
        self.value[5].set("YY-MM-DD")
        #Create Frame command
        command_frame = LabelFrame(self.master,text="COMMAND")
        command_frame.pack(expand="yes")

        #Button
        Button(command_frame,text="Thêm giá toa",command=self.themGiaToa).grid(column=0,row=0)
        Label(command_frame,width=22).grid(column=1,row=0)
        Button(command_frame,text="Xóa giá toa",command=self.xoaGiaToa).grid(column=2,row=0)
        Label(command_frame,width=22).grid(column=3,row=0)
        Button(command_frame,text="Sửa giá toa",command=self.suaGiaToa).grid(column=4,row=0)

        #BIND TREE
        self.tree.bind("<<TreeviewSelect>>",self.chooseItem)
       

        self.master.geometry("700x500")
        self.master.mainloop()

    def chooseItem(self,event):
        self.selected = self.tree.focus()
        a = self.tree.item(self.selected,"values")
        for i in range(len(a)):
            self.value[i].set(a[i])
        if(len(a)==3):
            self.value[3].set(0)
            self.value[4].set("YY-MM-DD")
            self.value[5].set("YY-MM-DD")
        
    def themGiaToa(self):
        trang_thai = None
        dung = 0
        for i in self.toa:
            if self.value[0].get() == i[0]:
                if(self.value[3].get()!=0 and self.value[4].get()!="YY-MM-DD" and self.value[5].get()!="YY-MM-DD"):
                    trang_thai  = insert_NKGT(self.value[0].get(),
                                            self.value[3].get(),
                                            self.value[4].get(),
                                            self.value[5].get())
                    break
            dung+=1
        print('trang_thai: ', trang_thai)
        if trang_thai == True :
            tam = ""
            try:
                tam = str(dung)+"."+str(self.chua[dung]+1)
            except:
                con.rollback()
            print('tam: ', tam)
            self.chua[dung]+=1
            messagebox.showinfo("THÔNG BÁO","THÊM THÀNH CÔNG")
            try:
                self.tree.insert(self.parent_Toa[dung],index='end',iid=tam,values=(self.toa[dung][0],
                                                                                self.toa[dung][1],
                                                                                self.toa[dung][2],
                                                                                self.value[3].get(),
                                                                                self.value[4].get(),
                                                                                self.value[5].get()))
            except:
                con.rollback()
            self.value[1].set("")
            self.value[1].set("")
            self.value[2].set(0)
            self.value[3].set(0)
            self.value[4].set("YY-DD-MM")
            self.value[5].set("YY-MM-DD")
            con.commit()
        elif trang_thai == False:
            messagebox.showinfo("THÔNG BÁO","THÊM KHÔNG THÀNH CÔNG\nNGÀY KHÔNG HỢP LỆ")
        elif trang_thai == None:
            messagebox.showinfo("THÔNG BÁO","THIẾU THUỘC TÍNH")

    def xoaGiaToa(self):
        try:
            self.selected
        except:
            print("123")
            return
        a = self.tree.item(self.selected,"values")
        if(len(a)==3):
            messagebox.showinfo("THÔNG BÁO","XOÁ KHÔNG THÀNH CÔNG")
        else:
            trang_thai = delete_NKGT(a[0],a[4])
            if trang_thai:
                try:
                    self.tree.delete(self.selected)
                except:
                    messagebox.showinfo("THÔNG BÁO","XOÁ KHÔNG THÀNH CÔNG")
                    con.rollback()
                messagebox.showinfo("THÔNG BÁO","XÓA THÀNH CÔNG")
                con.commit()
        self.value[1].set("")
        self.value[1].set("")
        self.value[2].set(0)
        self.value[3].set(0)
        self.value[4].set("YY-MM-DD")
        self.value[5].set("YY-MM-DD")

    def suaGiaToa(self):
        try:
            self.selected
        except:
            return
        value = self.tree.item(self.selected,"value")
        if(len(value)==3):
            messagebox.showinfo("THÔNG BÁO","SỬA KHÔNG THÀNH CÔNG")
        else:
            if(value[3] != self.value[3].get() or value[4] != self.value[4].get() or value[5] != self.value[5].get()):
                trang_thai =  update_NKGT(value[0]
                                ,value[4]
                                ,value[5]
                                ,self.value[3].get()
                                ,self.value[4].get()
                                ,self.value[5].get())
                if trang_thai:
                    try:
                        self.tree.item(self.selected,value=(value[0],
                                                            value[1],
                                                            value[2],
                                                            self.value[3].get(),
                                                            self.value[4].get(),
                                                            self.value[5].get()))
                    except:
                        messagebox.showinfo("THÔNG BÁO","SỬA KHÔNG THÀNH CÔNG")
                        con.rollback()
                    messagebox.showinfo("THÔNG BÁO","SỬA THÀNH CÔNG")
                    con.commit()
                else:
                    messagebox.showinfo("THÔNG BÁO","SỬA KHÔNG THÀNH CÔNG\nNGÀY KHÔNG HỢP LỆ")

class QuanLyVeTau(Frame):
    def __init__(self,master):
        self.master=master
        self.display()
    
    def display(self):

        #Frame Treeview
        frame_tree = LabelFrame(self.master,text="VIEW")
        frame_tree.pack()

        tree_scroll = Scrollbar(frame_tree)
        tree_scroll.pack(side=RIGHT,fill=Y)

        #Add style
        style = ttk.Style()
        
        #ping a theme
        style.theme_use('default')

        #configure Treeview
        style.configure("Treeview",
            background='#D3D3D3',
            foreground='black',
            rowheight=25,
            fieldbackground='silver')

        #Change selected color
        style.map('Treeview',
            background=[('selected','red')])
        
        #Create Treeview
        self.tree = ttk.Treeview(frame_tree,
                                yscrollcommand=tree_scroll)
        self.tree.pack()

        self.tree['column']=("Mã chuyến đi","Mã tàu","Ga đi","Ga đến","Ngày khởi hành","Tên khách hàng","Ngày sinh","CMND","Mã vé","Trạng thái","Giá")
        
        self.tree.column("#0",stretch = NO,width=10)
        self.tree.column("Mã chuyến đi",width=80)
        self.tree.column("Mã tàu",width=50)
        self.tree.column("Ga đi",width=50)
        self.tree.column("Ga đến",width=50)
        self.tree.column("Ngày khởi hành",width=90)
        self.tree.column("Tên khách hàng",anchor=CENTER,width=90)
        self.tree.column("Ngày sinh",anchor=CENTER,width=80)
        self.tree.column("CMND",anchor=CENTER,width=80)
        self.tree.column("Mã vé",anchor=CENTER,width=80)
        self.tree.column("Trạng thái",anchor=CENTER,width=100)
        self.tree.column("Giá",anchor=E,width=80)

        self.tree.heading("Mã chuyến đi",text="Mã chuyến đi")
        self.tree.heading("Mã tàu",text="Mã tàu")
        self.tree.heading("Ga đi",text="Ga đi")
        self.tree.heading("Ga đến",text="Ga đến")
        self.tree.heading("Ngày khởi hành",text="Ngày khởi hành")
        self.tree.heading("Tên khách hàng",text="Tên khách hàng")
        self.tree.heading("Ngày sinh",text="Ngày sinh")
        self.tree.heading("CMND",text="CMND")
        self.tree.heading("Mã vé",text="Mã vé")
        self.tree.heading("Trạng thái",text="Trạng thái")
        self.tree.heading("Giá",text="Giá")

        cd = select_CD_all()
        self.parent = []
        self.kh = []
        self.IID = 0

        for i in cd:
            self.parent.append(self.tree.insert("","end",self.IID,value=i))
            self.kh.append([])
            kh = select_KH_thanhToan(i[0])
            self.kh[self.IID]=kh
            dem = 1/10
            for j in kh :
                tam = dem +self.IID
                self.tree.insert(self.parent[self.IID],"end",tam,value= ("","","","","",
                                                                        j[0],
                                                                        j[1],
                                                                        j[2],
                                                                        j[3],
                                                                        j[4],
                                                                        j[5]
                                                                        ))
                dem = dem+1/10
            kh= select_KH_DatTruoc(i[0])
            print(kh)
            for j in kh :
                tam = dem +self.IID
                self.tree.insert(self.parent[self.IID],"end",tam,value= ("","","","","",
                                                                        j[0],
                                                                        j[1],
                                                                        j[2],
                                                                        j[3],
                                                                        j[4],
                                                                        j[5]
                                                                        ))
                self.kh[self.IID].append(j)
                dem = dem+1/10
            self.IID += 1

        frame = Frame(self.master)
        frame.pack()

        Label(frame,text="Tổng giá tiền").grid(column=0,row=0,sticky=E)
        self.tongGia=Label(frame,text="")
        self.tongGia.grid(column=1,row=0,sticky=E)
        Label(frame,text="VND").grid(column=2,row=0,stick=E)
        Label(frame,text="",width=10).grid(column=3,row=0)
        Label(frame,text="Số vé đã thanh toán").grid(column=4,row=0)
        self.tongSoVe = Label(frame,text="")
        self.tongSoVe.grid(column=5,row=0)

        self.tree.bind("<<TreeviewSelect>>",self.chon)

        self.master.geometry("1000x400")
        self.master.mainloop


    def chon(self,e):
        selected = self.tree.focus()
        try: 
         selected = int(selected)
        except:
            return
        tongGia = 0
        demVe = 0
        for i in self.kh[selected]:
            if i[4] == "Đã mua":
                tongGia += i[5]
                demVe+=1
        chuoi= str(demVe)+"/"+str(len(self.kh[selected]))
        self.tongSoVe['text']=chuoi
        self.tongGia['text']=tongGia

class QuanLyNhanVien(Frame):
    def __init__(self,master):
        self.master=master
        self.display()

    def display(self):

        frame_tree = LabelFrame(self.master,text="VIEW")
        frame_tree.pack()

        tree_scroll = Scrollbar(frame_tree)
        tree_scroll.pack(side=RIGHT,fill=Y)

        #Add style
        style = ttk.Style()
        
        #ping a theme
        style.theme_use('default')

        #configure Treeview
        style.configure("Treeview",
            background='#D3D3D3',
            foreground='black',
            rowheight=25,
            fieldbackground='silver')

        #Change selected color
        style.map('Treeview',
            background=[('selected','red')])
        
        #Create Treeview
        self.tree = ttk.Treeview(frame_tree,
                                yscrollcommand=tree_scroll)
        self.tree.pack()

        self.tree['column']= ('Tên tài khoản','Mật khẩu','Tên nhân viên','Ngày sinh','CMND','Số điện thoại','Chức vụ')

        self.tree.column("#0",width=0,stretch=NO)
        self.tree.column('Tên tài khoản',width=80)
        self.tree.column('Mật khẩu',width=80)
        self.tree.column('Tên nhân viên',width=80)
        self.tree.column('Ngày sinh',width=80)
        self.tree.column("CMND",width=50)
        self.tree.column("Số điện thoại",width=80)
        self.tree.column("Chức vụ",width=80)

        self.tree.heading("Tên tài khoản",text="Tên tài khoản")
        self.tree.heading("Mật khẩu",text="Mật khẩu")
        self.tree.heading("Tên nhân viên",text="Tên nhân viên")
        self.tree.heading("Ngày sinh",text="Ngày sinh")
        self.tree.heading("CMND",text="CMND")
        self.tree.heading("Số điện thoại",text="Số điện thoại")
        self.tree.heading("Chức vụ",text="Chức vụ")

        nv = select_NV_all()
        self.iid = 0
        for i in nv:
            try:
                self.tree.insert("","end",self.iid,value=nv[self.iid])
            except:
                print(i)
                self.tree.insert("","end",self.iid,value=i)
            self.iid+=1

        frame_record = LabelFrame(self.master,text="RECORD")
        frame_record.pack()

        Label(frame_record,text="Tên tài khoản").grid(column=0,row=0,sticky=W)
        Label(frame_record,text="Mật khẩu").grid(column=2,row=0,sticky=W)
        Label(frame_record,text="Tên nhân viên").grid(column=0,row=1,sticky=W)
        Label(frame_record,text="Ngày sinh").grid(column=2,row=1,sticky=W)
        Label(frame_record,text="CMND").grid(column=0,row=2,sticky=W)
        Label(frame_record,text="Số điện thoại").grid(column=2,row=2,sticky=W)
        Label(frame_record,text="Chức vụ").grid(column=0,row=3,sticky=E,columnspan=2)

        self.value = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        self.chucVu = ["Nhân viên",
                "Quản trị viên"]


        Entry(frame_record,textvariable=self.value[0]).grid(column=1,row=0)
        Entry(frame_record,textvariable=self.value[1]).grid(column=3,row=0)
        Entry(frame_record,textvariable=self.value[2]).grid(column=1,row=1)
        Entry(frame_record,textvariable=self.value[3]).grid(column=3,row=1)
        Entry(frame_record,textvariable=self.value[4]).grid(column=1,row=2)
        Entry(frame_record,textvariable=self.value[5]).grid(column=3,row=2)
        ttk.Combobox(frame_record,textvariable=self.value[6],values=self.chucVu).grid(column=2,row=3,columnspan=2,sticky=W)



        frame_command = LabelFrame(self.master,text="COMMAND")
        frame_command.pack()

        Button(frame_command,text="Thêm nhân viên",command=self.themNhanVien).grid(column=0,row=0)
        Button(frame_command,text="Sửa nhân viên",command=self.suaNhanVien).grid(column=2,row=0)
        Button(frame_command,text="Xóa nhân viên",command=self.xoaNhanVien).grid(column=4,row=0)
        self.tree.bind("<<TreeviewSelect>>",self.chon)

        self.master.geometry("600x450")
        self.master.mainloop

    def chon(self,e):
        self.selected = self.tree.focus()
        value=self.tree.item(self.selected,'value')
        for i in range(7):
            self.value[i].set(value[i])

    def themNhanVien(self):
        trangThai = True
        for i in self.value:
            if i.get() == "":
                trangThai == False
                break
        if self.value[6].get() not in self.chucVu:
            messagebox.showerror("THÔNG BÁO","KHÔNG CÓ CHỨC VỤ NÀY")
            return
        if trangThai == False:
            messagebox.showerror("THÔNG BÁO","NHẬP THIẾU THÔNG TIN")
        else:
            thanh_cong = insert_NV(self.value[0].get(),
                                    self.value[1].get(),
                                    self.value[2].get(),
                                    self.value[3].get(),
                                    self.value[4].get(),
                                    self.value[5].get(),
                                    self.value[6].get())
            if thanh_cong == True:
                self.tree.insert("","end",self.iid,value=(self.value[0].get(),
                                                        self.value[1].get(),
                                                        self.value[2].get(),
                                                        self.value[3].get(),
                                                        self.value[4].get(),
                                                        self.value[5].get(),
                                                        self.value[6].get()))
                self.iid+=1
                messagebox.showinfo("THÔNG BÁO","THÊM NHÂN VIÊN THÀNH CÔNG")
                self.setLaiEntry()
                con.commit()
            else:
                messagebox.showerror("THÔNG BÁO",thanh_cong)
                con.rollback()

    def xoaNhanVien(self):
        try:
            value=self.tree.item(self.selected,'value')
        except:
            return
        state = messagebox.askquestion("THÔNG BÁO","BẠN CÓ MUỐN XÓA NHÂN VIÊN NÀY KHÔNG!")
        if state:
            thanhCong = delete_NV(value[0])
            if thanhCong == True:
                messagebox.showinfo("THÔNG BÁO","XÓA THÀNH CÔNG")
                self.tree.delete(self.selected)
                con.commit()
                self.setLaiEntry
            else:
                messagebox.showerror("THÔNG BÁO",thanhCong)
    
    def suaNhanVien(self):
        try:
            value=self.tree.item(self.selected,'value')
        except:
            return
        state = messagebox.askquestion("THÔNG BÁO","BẠN CÓ MUỐN SỬA NHÂN VIÊN NÀY KHÔNG!")
        trangThai = False
        if state:
            for i in range(7):
                if self.value[i].get() != value[i]:
                    trangThai = True
                    break
            if trangThai:
                if self.value[6].get() not in self.chucVu:
                    messagebox.showerror("THÔNG BÁO","KHÔNG CÓ CHỨC VỤ NÀY")
                    return
                thanh_cong = update_NV(value[0]
                                    ,self.value[0].get()
                                    ,self.value[1].get()
                                    ,self.value[2].get()
                                    ,self.value[3].get()
                                    ,self.value[4].get()
                                    ,self.value[5].get()
                                    ,self.value[6].get())
                if thanh_cong == True:
                    messagebox.showinfo("THÔNG BÁO","SỬA THÀNH CÔNG")
                    self.tree.item(self.selected,value=(self.value[0].get()
                                                        ,self.value[1].get()
                                                        ,self.value[2].get()
                                                        ,self.value[3].get()
                                                        ,self.value[4].get()
                                                        ,self.value[5].get()
                                                        ,self.value[6].get()))
                    con.commit()
                    self.setLaiEntry()
                else :
                    messagebox.showerror("THÔNG BÁO",thanh_cong)
    def setLaiEntry(self):
        self.value[0].set("")
        self.value[1].set("")
        self.value[2].set("")
        self.value[3].set("")
        self.value[4].set("")
        self.value[5].set("")
        self.value[6].set("")


DangNhap(Tk())