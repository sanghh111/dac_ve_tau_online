import sqlite3
from datetime import date


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
    cau_truy_van += '\nAnd maGaXuatPhat = "{Ga_di}"'.format(Ga_di=ga_di)    
    cau_truy_van += '\nAnd maGaNoiDen = "{Ga_den}"'.format(Ga_den=ga_den)
    print(cau_truy_van)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    return result


def select_Ga(cur):
    cau_truy_van = '''Select maGa,tenGa
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

def select_tau(cur):
    cau_truy_van = '''Select*
    from Tau 
    '''
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    return result

def insert_ghe(con, cur, ma,soCho):
    cau_truy_van = '''Insert into "Cho ngoi"
Values'''
    for i in range(soCho-1):
        maThamThoi = ma
        maThamThoi += str(i+1)
        cau_truy_van += '''('{maChoNgoi}','{maToa}'),\n'''.format(
            maChoNgoi=maThamThoi, maToa=ma)
    cau_truy_van += '''('{maChoNgoi}{_soCho}','{maToa}');'''.format(maChoNgoi=ma, maToa=ma,_soCho=soCho)
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
    print('cau_truy_van: ', cau_truy_van)
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    return result


def Select_Ve_maVe(cur, maVe):
    cau_truy_van = '''Select 
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
(SELECT tenToa
From Toa
Where A.maToa=maToa)as "ten Toa",
A.maTau,
A.trangThai,
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


def Select_maKH_cmnd(cur, cmnd):
    cau_truy_van = '''Select maKH
from "Khach hang"
Where Cmnd = '{Cmnd}';'''.format(Cmnd=cmnd)
    try:
        result = cur.execute(cau_truy_van).fetchone()
    except:
        result = None
    # if result == None and result == "":
    if result:
        return result[0]



def select_kh_cmnd_all(cmnd):
    cau_truy_van = '''Select *
    from "Khach hang"
    Where Cmnd = '{Cmnd}';'''.format(Cmnd=cmnd)
    try:
        result = cur.execute(cau_truy_van).fetchone()
    except:
        result = None
    if result:
        return result

def Insert_NKTT(con, cur, maVe, maKH):
    day = str(date.today())
    cau_truy_van = '''Insert into "Nhat Ky Thanh Toan"
Values("{ma_ve}","{ma_kh}","{Day}")'''.format(
        ma_ve=maVe, ma_kh=maKH, Day=day)
    print('cau_truy_van: ', cau_truy_van)
    try:
        cur.execute(cau_truy_van)
        return True
    except Exception as e:
        return e

def insert_NKDC(con, cur, maKH, maVe, ngayDat, ngayHetHan)->bool:
    maDC = maKH + "-" + maVe
    cau_truy_van = '''Insert into "Nhat ky dat cho"(maDC,maKH,maVe,ngayDat,ngayHetHan)
Values("{ma_dc}","{ma_kh}","{ma_ve}","{ngay_dat}","{ngay_het_han}")'''.format(
        ma_dc=maDC, ma_kh=maKH, ma_ve=maVe, ngay_dat=ngayDat, ngay_het_han=ngayHetHan
    )
    print('cau_truy_van: ', cau_truy_van)
    try:
        cur.execute(cau_truy_van)
        return True
    except:
        return False 
def select_NKDV_maVe(cur,madc):
    cau_truy_van = '''Select maKH,maVe,ngayHetHan
from "Nhat ky dat cho"
where maDC="{maDC}"'''.format(maDC=madc)
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    if result:
        return result[0]

def select_NKDV_maKH(maKH):
    cau_truy_van = '''Select maVe,ngayDat,ngayHetHan,trangThai
    From "Nhat ky dat cho"
    Where maKH = "{ma}"
        AND trangThai = "Chưa thanh toán"
    '''.format(ma=maKH)
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    if result:
        return result

def huy_NKDV(maVe,maKH):
    cau_truy_van = '''Update "Nhat ky dat cho"
    Set trangThai = "Hủy vé"
    Where maVe = "{mv}"
    And maKH = "{kh}"
    '''.format(mv=maVe,kh=maKH)
    try:
        result = cur.execute(cau_truy_van)
        return True
    except Exception as e:
        return e
        
def select_kh_maKh(cur,maKH):
    cau_truy_van = '''Select tenKh,Cmnd,ngaySinh
from "Khach hang"
Where maKH = "{ma}"'''.format(ma=maKH)
    try:
        result = cur.execute(cau_truy_van).fetchone()
    except:
        result = None
    if result:
        return result

def Insert_Nv(cur,con,tenTk,passWorld,tenNV,ngaySinh,CMND,Sdt,chucVu):
    cau_truy_van ='''Insert into "Nhan vien"
Values("{tentk}","{Pass}","{ten}","{ngaysinh}","{cmnd}",{sdt},"{chucvu}")
'''.format(tentk=tenTk,Pass=passWorld,ten=tenNV,ngaysinh=ngaySinh,sdt=Sdt,chucvu=chucVu,cmnd=CMND)
    print(cau_truy_van)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        con.commit()
        return True
    else:
        return False

def checkPass(cur,tenTk):
    cau_truy_van='''Select matKhau
From "Nhan vien"
Where tenTk = "{tk}"
'''.format(tk=tenTk)
    try:
        result = cur.execute(cau_truy_van).fetchone()
    except:
        result = None
    if result:
        return result[0]

def select_thong_tinNV(tenTk):
    cau_truy_van='''Select *
From "Nhan vien"
Where tenTk = "{tk}"
'''.format(tk=tenTk)
    try:
        result = cur.execute(cau_truy_van).fetchone()
    except:
        result = None
    if result:
        return result

def insert_tau(con,cur,maTau,tenTau):
    cau_truy_van =  '''Insert into "Tau"
Values("{ma}","{ten}")'''.format(ma=maTau,ten=tenTau)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        con.commit()
        return True
    return False

def delete_tau(maTau):
    cau_truy_van = '''Delete from "Tau"
Where maTau = '{ma}'
'''.format(ma=maTau)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        con.commit()
        return True
    else :
        return False

def update_tau(maTau,gt1,gt2):
    cau_truy_van = '''Update  "Tau"
SET '''
    if gt1:
        cau_truy_van += 'maTau ="{ma}"'.format(ma=gt1)
    if gt2:
        if gt1:
            cau_truy_van+=",\n"
        cau_truy_van += 'tenTau ="{ma}"\n'.format(ma=gt2)
    if cau_truy_van != '''Update  "Tau
SET "''':
        cau_truy_van+='''Where maTau = "{ma}"'''.format(ma=maTau)
        print('cau_truy_van: ', cau_truy_van)
        try:
            result = cur.execute(cau_truy_van)
        except:
            result = None
        if result:
            con.commit()
            return True
        else :
            return False

def select_Ga_all(cur):
    cau_truy_van = '''Select *
from "Ga Tau"'''
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    return result

def insert_ga(maGa,tenGa,viTri,chieuDai,chieuRong):
    cau_truy_van =  '''Insert into "Ga Tau"
Values("{ma}","{ten}","{vt}",{dai},{rong})'''.format(ma=maGa,
                                                    ten=tenGa,
                                                    vt=viTri,
                                                    dai=chieuDai,
                                                    rong=chieuRong)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        con.commit()
        return True
    return False

def delete_Ga(maGa):
    cau_truy_van = '''Delete from "Ga Tau"
Where maGa = '{ma}'
'''.format(ma=maGa)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        con.commit()
        return True
    else :
        return False

def update_ga(Ma,maGa,tenGa,viTri,dai,rong):
    cau_truy_van = '''Update "Ga Tau"
SET maGa = "{ma}",
tenGa = "{ten}",
viTri = "{vt}",
chieuDai = {Dai},
chieuRong = {Rong}
Where maGa = "{maga}"'''.format(ma=maGa,
                            ten=tenGa,
                            vt=viTri,
                            Dai=dai,
                            Rong=rong,
                            maga=Ma)
    print('cau_truy_van: ', cau_truy_van)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        con.commit()
        return True

def select_NKGT(maToa):
    cau_truy_van = '''Select *
From "Nhat Ky gia toa"
Where maToa = "{ma}"
'''.format(ma=maToa)
    try:
        reslut = cur.execute(cau_truy_van).fetchall()
    except:
        reslut = None
    return reslut

def insert_NKGT(maToa,gia,nbd,nkt):
    print("Insert")
    cau_truy_van = '''Insert into "Nhat Ky gia toa"
Values("{ma}",{_gia},"{_nbd}","{_nkt}")
'''.format(ma=maToa,_gia=gia,_nbd=nbd,_nkt=nkt)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        return True
    else:
        return False

def delete_NKGT(maToa,nbd):
    cau_truy_van=''' Delete From "Nhat Ky gia toa"
Where maToa="{ma}"
and ngayBatDau = "{_nbd}"
'''.format(ma=maToa,_nbd=nbd)
    try:
        result = cur.execute(cau_truy_van)
    except:
        result = None
    if result:
        return True
    else :
        return False

def update_NKGT(maToa,gt1,gt2,gia,nbd,nkt):
    cau_truy_van = '''Update "Nhat Ky gia toa"
    SET gia={_gia},
    ngayBatDau = "{_nbd}",
    ngayKetThuc = "{_nkt}"
    where maToa="{ma}"
    and ngayBatDau = "{_nbdb}"
    and ngayKetThuc = "{_nktb}"
    '''.format(ma=maToa,_gia=gia,_nbd=nbd,_nkt=nkt,_nbdb=gt1,_nktb=gt2)
    print(cau_truy_van)
    try:
        result = cur.execute(cau_truy_van)
    except Exception as e:
        print(e)
        result = None
    if result:
        return True
    else :
        return False

def select_CD_all():
    cau_truy_van='''Select *
    From "ChuyenDI"'''
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    return result

def select_tau_ma():
    cau_truy_van='''Select maTau
    From "Tau"
    '''
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    return result

def insert_CD(maCD,maTau,maGaXP,maGaDen,ngayKH):
    cau_truy_van = '''Insert into "ChuyenDI"
    values("{_maCD}","{_maTau}","{_maGaXP}","{_maGaDen}","{_ngayKH}")
    '''.format(_maCD=maCD,_maTau=maTau,_maGaXP=maGaXP,_maGaDen=maGaDen,_ngayKH=ngayKH)
    try:
        result = cur.execute(cau_truy_van)
        return True
    except Exception as e:
        result = e
        return e

def delete_CD(maCD):
    cau_truy_van = '''DELETE FROm ChuyenDi
    WHERE maCD="{ma}"'''.format(ma=maCD)
    try:
        result = cur.execute(cau_truy_van)
        result = True
    except Exception as e:
        result =e
    return result

def Update_CD(maCD,maTau,maGXP,maGD,ngayKH,MACD,MATAU,NGAYKH):
    cau_truy_van='''Update "ChuyenDI"
    Set maCD ="{_maCD}",
        maTau="{_maTau}",
        maGaXuatPhat="{_maGXP}",
        maGaNoiDen="{_maGD}",
        ngayKhoiHanh="{_ngayKH}"
    WHere maCD ="{_ma}"
    AND maTau="{_tau}"
    AND ngayKhoiHanh="{_ngay}"
    '''.format(_maCD=maCD,_maTau=maTau,_maGXP=maGXP,_ngayKH=ngayKH,_maGD=maGD,
                _ma=MACD,_tau=MATAU,_ngay=NGAYKH)
    try:
        cur.execute(cau_truy_van)
        result = True
        print("a")
    except Exception as e:
        result = e
    return result

def select_KH_thanhToan(maCD):
    cau_truy_van = '''select C.tenKH,C.ngaySinh,C.Cmnd,A.maVe,B.trangThai,B.Gia
    from "Nhat Ky thanh toan" as A
    INNER join Ve as B
    on A.maVe=B.maVe
    Inner join "Khach hang" as C
    on A.maKH = C.maKH
    Where maCD = "{ma}"'''.format(ma=maCD)
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    return result

def select_KH_DatTruoc(maCD):
    cau_truy_van= '''select C.tenKH,C.ngaySinh,C.Cmnd,A.maVe,B.trangThai,B.Gia
    from "Nhat ky dat cho" as A
    INNER join Ve as B
    on A.maVe=B.maVe
    Inner join "Khach hang" as C
    on A.maKH = C.maKH
    Where maCD = "{ma}" And
	B.trangThai<> "Đã mua"'''.format(ma=maCD)
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    return result

def select_NV_all():
    cau_truy_van = '''Select *
    From "Nhan vien"
    '''
    try:
        result = cur.execute(cau_truy_van).fetchall()
    except:
        result = None
    return result

def insert_NV(maNV,matKhau,tenNV,ngaySinh,CMND,sdt,chucVu):
    cau_truy_van = '''Insert into "Nhan vien"
    values("{ma}","{mk}","{ten}","{ns}",{cm},"{_sdt}","{cv}")
    '''.format(ma=maNV,mk=matKhau,ten=tenNV,ns=ngaySinh,cm=CMND,_sdt=sdt,cv=chucVu)
    try:
        cur.execute(cau_truy_van)
        return True
    except Exception as e:
        return e

def delete_NV(tk):
    cau_truy_van = '''Delete From "Nhan vien"
    Where tenTk = "{_tk}"
    '''.format(_tk=tk)
    try:
        cur.execute(cau_truy_van)
        return True
    except Exception as e:
        return e

def update_NV(tkc,tkm,matKhau,tenNV,ngaySinh,cmnd,sdt,chucVu):
    cau_truy_van = '''Update "Nhan vien"
    Set
    tenTk = "{_tkm}",
    matKhau = "{mk}",
    tenNV = "{ten}",
    ngaySinh = "{ngay}",
    cmnd = "{CMND}",
    sdt = "{_sdt}",
    chucVu = "{cv}"
    WHERE tenTk =  "{_tkc}"
    '''.format(_tkc=tkc,_tkm=tkm,mk=matKhau,ten=tenNV,ngay=ngaySinh,CMND=cmnd,_sdt=sdt,cv=chucVu)
    try: 
        cur.execute(cau_truy_van)
        return True
    except Exception as e:
        return e

# print(date.now())

con, cur = connect_DB('dac_ve_tau.db')
# con.rollback()
# a = checkPass(cur,"sang")
# print(a)
# a= Insert_Nv(cur,con,"sang","123","Tấn Sang","2000-04-08","654665","4656565","Quản trị viên")
# a= select_NKDV_maVe(cur,"KH-4-SG-HN01-58")
# a=Select_maKH_cmnd(cur,"122")
# a=Select_Ve_maVe(cur,"SG-HN01-2")
# Insert_KH(cur,con,"Loc","123","2000-04-08")
# Insert_Ve(cur,con,'SG-HN01','NCDH','K6C',500000,42,168)
# insert_ghe(con,cur,"K6C",42)
# a=select_toa_tau(cur)