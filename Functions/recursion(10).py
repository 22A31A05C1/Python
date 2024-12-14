def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
def arm(n,count):
    if n==0:
        return 0
    d=n%10
    return d**count+arm(n//10,count)
def armstrong(n):
    c=count(n)
    return n==arm(n,c)
n=int(input("Enter a number:"))
if armstrong(n):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")