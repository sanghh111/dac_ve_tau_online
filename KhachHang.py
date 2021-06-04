from db import *
# import re
# import Ve
class KhachHang():

    def __init__(self):
        self.tenKH = None
        self.maKH = None
        self.cmnd = None
        self.ngaySinh = None

    def setTenKH(self, tenKH):
        self.tenKH = tenKH

    def setmaKH(self,maKH):
        self.maKH = maKH
        self.setTTDB()

    def themDB(self):
        pass

    def setCMND(self, cmnd):
        self.cmnd = cmnd

    def setNgaySinh(self, ngay,thang,nam):
        self.ngaySinh='''{ngay}-{thang}-{nam}'''.format(ngay = ngay,
                                                        thang = thang,
                                                        nam = nam)

    def __str__(self) -> str:
        return '''Tên: {ten}
CMND: {cmnd}
Ngày sinh: {ngaySinh}'''.format(ten=self.tenKH,
                                cmnd=self.cmnd,
                                ngaySinh=self.ngaySinh)

    def timMaKH(self):
        maKH = Select_maKH_cmnd(cur,self.cmnd)
        if maKH :
            self.maKH =maKH
            return maKH
        else: 
            maKH=Insert_KH(cur,con,self.tenKH,self.cmnd,self.ngaySinh)
            if maKH:
                return maKH
            else :
                return None

    def setTTDB(self):
        kh=select_kh_maKh(cur,self.maKH)
        self.tenKH = kh[0]
        self.maKH = kh[1]
        self.ngaySinh = kh[2]
# Ve("SG-HN01-200")