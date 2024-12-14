def fun(n):
    if n==0:
        return 0
    fun(n-1)
    print(n) 
x=int(input("Enter the no:"))
fun(x)

def fun(n):
    if n==0:
        return 0
    print(n)
    fun(n-1) 
x=int(input("Enter the no:"))
fun(x)