def rev(n,re=0):
    if n==0:
        return re
    else:
        d=n%10
        re=re*10+d
        return rev(n//10,re)
n=int(input("Enter a number:"))
print(rev(n))