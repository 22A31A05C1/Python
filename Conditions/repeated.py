s=input()
res=[]
for i in range(len(s)):
    if i>2 or not(s[i]==s[i-1]==s[i-2]):
        res.append(s[i])
print("".join(res))