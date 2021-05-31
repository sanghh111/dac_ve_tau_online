import sqlite3


def connect_DB(dbfile):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    return con, cur


def select_CD(cur, ngay, ga_di, ga_den):
    cau_truy_van = '''Select maCD,(SELECT tenGa
From "Ga Tau"
WHERE A.maGaXuatPhat = maGa) as "Ga Xuat Phat "
,(SELECT tenGa
From "Ga Tau"
WHERE A.maGaNoiDen = maGa) as "Ga Noi Den "
,ngayKhoiHanh
From ChuyenDi as A
Where ngayKhoiHanh in ("{Ngay}")'''.format(Ngay=ngay)
    if(ga_di != 'Chọn'):
        cau_truy_van += '\nAnd maGaXuatPhat = "{Ga_di}"'.format(Ga_di=ga_di)
    if(ga_den != "Chọn"):
        cau_truy_van += '\nAnd maGaNoiDen = "{Ga_den}"'.format(Ga_den=ga_den)
    # print(cau_truy_van)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    return result


def select_Ga(cur):
    cau_truy_van = '''Select*
from "Ga Tau"'''
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    return result


def select_toa_tau(cur):
    cau_truy_van = '''Select*
    from Toa 
    '''
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    return result


def insert_ghe(con, cur, ma):
    cau_truy_van = '''Insert into "Cho ngoi"
Values'''
    for i in range(27):
        maThamThoi = ma
        maThamThoi += str(i+1)
        cau_truy_van += '''('{maChoNgoi}','{maToa}'),\n'''.format(
            maChoNgoi=maThamThoi, maToa=ma)
    cau_truy_van += '''('{maChoNgoi}28','{maToa}');'''.format(maChoNgoi=ma, maToa=ma)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if(result):
        print('ok')
        con.commit()
    else:
        print('no ok')
    print(cau_truy_van)


def Insert_Ve(cur, con, maCD, maToa, maTau, Gia, soLg, viTri):
    cau_truy_van = '''Insert Into "Ve"
Values'''
    for i in range(soLg-1):
        maCho = maToa+str(i+1+viTri)
        ma_ve = maCD+"-"+str(i+1+viTri)
        cau_truy_van += "('{ma_Ve}','{ma_CD}','{ma_Cho}','{ma_Toa}','{ma_tau}','Trống',{gia}),\n".format(
            ma_Ve=ma_ve, ma_CD=maCD, ma_Cho=maCho, ma_Toa=maToa, ma_tau=maTau, gia=Gia
        )
    maCho = maToa+str(soLg+viTri)
    ma_ve = maCD+"-"+str(soLg+viTri)
    cau_truy_van += "('{ma_Ve}','{ma_CD}','{ma_Cho}','{ma_Toa}','{ma_tau}','Trống',{gia});".format(
        ma_Ve=ma_ve, ma_CD=maCD, ma_Cho=maCho, ma_Toa=maToa, ma_tau=maTau, gia=Gia
    )
    print(cau_truy_van)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if(result):
        print("thanh cong")
        con.commit()
    else:
        print("That bai")


def Select_Ve(cur, maCD):
    cau_truy_van = '''Select maVe
,maToa
,(Select B.'tenToa'
from Toa as B
WHERE A.maToa=B.maToa)as "Tên toa"
,TrangThai
,Gia
From "Ve" as A
Where maCD="{maCd}"'''.format(maCd=maCD)
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    return result


def Select_Ve_maVe(cur, maVe):
    cau_truy_van = '''Select 
A.maVe,
B.maCD,
(Select tenGa
From "Ga Tau"
Where B.maGaXuatPhat = maGa) as "Ga xuat phat",
(Select tenGa
From "Ga Tau"
Where B.maGaNoiDen = maGa) as "Ga den",
B.ngayKhoiHanh,
A.maCho,
A.maToa,
A.maTau,
A.Gia
From Ve as A 
inner join "ChuyenDi" as B
on A.maCD = B.maCD
Where  maVe = "{mave}"'''.format(mave=maVe)
    try:
        result = cur.execute(cau_truy_van).fetchone()
    except:
        result = None
    return result


def lay_maKH(cur):
    cau_truy_van = '''Select dem
From  "Khach hang"
Where dem =  (Select max(dem)
From "Khach hang")'''
    try:
        result = cur.execute(cau_truy_van).fetchone()
    except:
        result = None
    return result


def Insert_KH(cur, con, tenKH, cmnd, ngaySinh):
    dem = lay_maKH(cur)
    if dem:
        dem = dem[0]+1
    else:
        dem = 1
    makh = "KH-"+str(dem)
    cau_truy_van = '''Insert into "Khach hang"
values("{ma}","{ten}","{CMND}","{ngay}",{so})'''.format(ma=makh, ten=tenKH, CMND=cmnd, ngay=ngaySinh, so=dem)
    print(cau_truy_van)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        con.commit()
        return makh
    else:
        print("That bai")
        return None
# con,cur = connect_DB('dac_ve_tau.db')
# a=Select_Ve_maVe(cur,"SG-HN01-2")
# print(a)
# Insert_KH(cur,con,"Loc","1231313","2000-04-08")
# Insert_Ve(cur,con,'SG-HN01','NCDH','K6C',500000,42,168)
# insert_ghe(con,cur,"K4C")
# a=select_toa_tau(cur)
# print(a)
# a=select_Ga(cur)
# print(len(a.fetchall()))
# if(a):
#     print(a.fetchall())
# a=select_CD(cur,'2021-5-12',"SG","Chọn")
# print(a.fetchall())
# for i in a:
#     print(i)
