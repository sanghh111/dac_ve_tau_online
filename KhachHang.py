from db import *
# import re
# import Ve
class KhachHang():

    def __init__(self):
        self.tenKH = None
        self.maKH = None
        self.cmnd = None
        self.ngaySinh = None
        self.trangThai = False

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


    def setCMND_DB(self,cmnd):
        trangThai = select_kh_cmnd_all(cmnd)
        print('trangThai: ', trangThai)
        if trangThai:
            self.cmnd=cmnd
            self.maKH = trangThai[0]
            self.tenKH = trangThai[1]
            self.ngaySinh = trangThai[3]
            self.trangThai = True
        else:
            self.trangThai = False

    def isNULL(self):
        return not self.trangThai

    def getCacVeDat(self):
        return select_NKDV_maKH(self.maKH)
    
    def huyVeDat(self,maVe) -> bool:
        for i in maVe:
            dung = huy_NKDV(i,self.maKH)
            if dung != True:
                con.rollback()
                return False
            con.commit()
            return True
# Ve("SG-HN01-200")
# a = KhachHang(