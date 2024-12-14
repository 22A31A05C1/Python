password=input()
c=0
l=len(password)
if not(l<=0 and l>=22):
    c+=1
uc,lc,d,sc,p=1,1,1,1,0
spl_count=0
for i in range(l):
    if password[i].isupper():
        uc=0
    if password[i].islower():
        lc=0
    if password[i].isdigit():
        d=0
    if password[i] in "!@#$%^&*":
        spl_count+=1
    if i+1<l and password[i]==password[i+1]:
        p+=1
if spl_count>=2:
    sc=0
c=uc+lc+d+sc+p
print("No of voilations are:",c)