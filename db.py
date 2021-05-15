import sqlite3
def connect_DB(dbfile):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    return con, cur

def select_CD(cur,ngay,ga_di,ga_den):
    cau_truy_van = '''Select maCD,(SELECT tenGa
From "Ga Tau"
WHERE A.maGaXuatPhat = maGa) as "Ga Xuat Phat "
,(SELECT tenGa
From "Ga Tau"
WHERE A.maGaNoiDen = maGa) as "Ga Noi Den "
,ngayKhoiHanh
From ChuyenDi as A
Where ngayKhoiHanh in ("{Ngay}")'''.format(Ngay=ngay)
    if(ga_di!='Chọn'):
        cau_truy_van+='\nAnd maGaXuatPhat = "{Ga_di}"'.format(Ga_di=ga_di)
    if(ga_den!="Chọn"):
        cau_truy_van+='\nAnd maGaNoiDen = "{Ga_den}"'.format(Ga_den=ga_den)
    # print(cau_truy_van)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result=None
    return result

def select_Ga(cur):
    cau_truy_van='''Select*
from "Ga Tau"'''
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    return result
# con,cur = connect_DB('dac_ve_tau.db')
# a=select_Ga(cur)
# print(len(a.fetchall()))
# if(a):
#     print(a.fetchall())
# a=select_CD(cur,'2021-5-12',"SG","Chọn")
# print(a.fetchall())
# for i in a:
#     print(i)