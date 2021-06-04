from db import *

class VeDat():
    def __init__(self,maVeDat):
        self.maVeDat = maVeDat
        self.kiemTraVeDat()

    def kiemTraVeDat(self):
        nkVe = select_NKDV_maVe(cur,self.maVeDat)
        if nkVe:
            self.coVe = True
            self.maKH = nkVe[0]
            self.maVe = nkVe[1]
            year = int(nkVe[2][0:4])
            month = int(nkVe[2][5:7])
            day = int(nkVe[2][8:10])
            self.ngayHetHan = date(year=year,month=month,day=day)
        else :
            self.coVe = False

    def isNull(self):
        return not(self.coVe)
    
    def get_maVe(self):
        return self.maVe

    def get_kh(self):
        return self.maKH