n=int(input())
r=0
while n:
    d=n%10
    r=r+d
    n//=10
flag=0
for i in range(2,int(r**0.5)+1):
    if r%i==0:
        flag=1
        break
if flag==0:
        print("Googly")
else:
        print("Not Googly")