def prime(n,i=2):
    if n<=1:
        return 0
    if n==2:
        return 1
    if n%i==0:
        return 0
    if i+1>n:
        return 1
    return prime(n,i+1)
n=int(input("Enter a number:"))
res=prime(n)
if res==1:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")