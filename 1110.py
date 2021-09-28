n=t=int(input())
count=0
while True:
    a=n//10
    b=n%10
    tot=a+b
    count+=1
    n=int(str(b)+str(tot%10))
    if(t==n):
        break
print(count)