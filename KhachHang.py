from db import *

class KhachHang():

    def __init__(self):
        self.tenKH = None
        self.maKH = None
        self.cmnd = None
        self.ngaySinh = None

    def setTenKH(self, tenKH):
        self.tenKH = tenKH

    def setmaKH(self):
        pass

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