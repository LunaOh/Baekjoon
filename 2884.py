h,m=map(int,input().split())
if m>=45:
    m=m-45
    h=h
elif m<45 and h>0:
    m=m+60-45
    h=h-1
elif h==0:
    m=m+60-45
    h=23
print(h,m)