# import KhachHang
from datetime import timedelta
import re
from tkinter import Label
from db import *
# from KhachHang import KhachHang


class Ve():
    def __init__(self, maVe):
        self.maVe = maVe
        self.setVe()

    def setVe(self):
        ve =  Select_Ve_maVe(cur,self.maVe)
        self.maCD = ve[0]
        self.gaDi = ve[1]
        self.gaDen = ve[2]
        self.ngayKhoiHanh = ve[3]
        self.maCho = ve[4]
        self.maToa = ve[5]
        self.tenToa = ve[6]
        self.maTau = ve[7]
        self.trangThai = ve[8]
        self.gia = ve[9]

    def getMaCD(self):
        return self.maCD

    def getGaDi(self):
        return self.gaDi

    def getGaDen(self):
        return self.gaDen

    def getNgayKhoiHanh(self):
        return self.ngayKhoiHanh

    def getmaCho(self):
        return self.maCho

    def getmaToa(self):
        return self.maToa

    def getmaTau(self):
        return self.maTau

    def getTrangThai(self):
        return self.trangThai

    def getGia(self):
        return self.gia

    def getSoGhe(self):
        heso =0
        if self.tenToa == 'Ngồi mềm điều hòa':
            heso = 0
        elif self.tenToa == 'Ngồi cứng điều hòa':
            heso = 64
        elif self.tenToa == 'Toa 4 chiều':
            heso = 64+80
        elif self.tenToa == 'Toa 6 chiều':
            heso = 80+64+24
        soGhe = self.maVe[len(self.maCD)+1:]
        soGhe = int(soGhe)
        return (soGhe-heso)

    def getTenToa(self):
        return self.tenToa

    def themKH(self,kh):
        self.kh= kh
        makh= kh.timMaKH()
        trangThai = Insert_NKTT(con,cur,self.maVe,makh)
        print('trangThai: ', trangThai)
        
    def chuyenDate(self):
        to_day = date.today()
        print(to_day)
        year = int(self.ngayKhoiHanh[0:4])
        month = int(self.ngayKhoiHanh[5:7])
        day =int(self.ngayKhoiHanh[8:10])
        veDate = date(year=year,month=month,day=day)
        delta= veDate - to_day
        delta=delta.days
        return delta

    def thanhToanSau(self,soNgay,kh):
        a=timedelta(days=soNgay)
        today = date.today()
        hetHan =today + a
        self.kh= kh
        makh= kh.timMaKH()
        trangThai = insert_NKDC(con,cur,makh,self.maVe,today,hetHan)
        print('trangThai: ', trangThai)

# a=Ve("SG-HN01-200")
# a.thanhToanSau(32)
# a.chuyenDate()
# b=a.getSoGhe()
# print(b)
# KhachHang