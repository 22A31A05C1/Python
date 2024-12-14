def fun(n,m):
    if n==0:
        return 0
    print(m)
    fun(n-1,m+1)
    if(m-1)!=0:
        print(m-1)
x,y=10,1
fun(x,y)