n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
c=[0]*max(vote)
for i in range(n):
    if age[i]>=18:
        c[vote[i]-1]+=1
sorted_c=sorted(c,reverse=True)
if len(c)>1 and sorted_c[0]==sorted_c[1]:
    print(-1)
else:
    print(c.index(sorted_c[0])+1)