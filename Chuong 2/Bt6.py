a=input('Ho ten: ')
c=int(input('So ngay cong: '))
b=int(input('Don gia ngay cong: '))
d=float(input('He so phu cap: '))
e=int(input('Tam ung: '))
Luong=round(c*b*d,1)
ThucLinh=round(Luong-e,1)
print('Nhan vien',a,end=", ")
print('Co tien luong=',Luong,sep="",end=", ")
print('Tam ung=',e," va",sep="",end=" ")

