from db import *


class NhanVien():
    def __init__(self,tenTK=None,matKhau=None):
        self.tenTK=tenTK
        self.matKhau = matKhau

    def dangNhap(self,tk,mk):
        matKhau = checkPass(cur,tk)
        if matKhau:
            self.tenTk=tk
            print(self.tenTk)
            self.matKhau = matKhau
            thong_tin = select_thong_tinNV(self.tenTk)
            # if(thong_tin):
            self.ten = thong_tin[0]
            self.tenNV=thong_tin[2]
            self.ngaySinh=thong_tin[3]
            self.cmnd = thong_tin[4]
            self.sdt = thong_tin[5]
            self.chucVu = thong_tin[6]
            return True
        else:
            return False

    def getTen(self):
        return self.ten

    def getChucVu(self):
        return self.chucVu

    def getTenNV(self):
        return self.tenNV

    def getNgaySinh(self):
        return self.ngaySinh

    def getCMND(self):
        return self.cmnd
    
    def getSDT(self):
        return self.sdt

    