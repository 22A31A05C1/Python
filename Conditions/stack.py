s=input()
stack=[]
for i in range(len(s)):
    if stack and s[i]==stack[-1]:
        stack.pop()
    else:
        stack.append(s[i])
print("".join(stack))