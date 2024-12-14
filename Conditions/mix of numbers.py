s=input()
k=len(s)-1
res=0
for c in s:
    res=res+(10**k)*ord(c)
    k-=1
print(res)