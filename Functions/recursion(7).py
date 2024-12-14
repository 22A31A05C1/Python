def fun(n):
    if n==0:
        return 1
    return n*fun(n-1)
x=int(input("Enter a number:"))
print(fun(x))