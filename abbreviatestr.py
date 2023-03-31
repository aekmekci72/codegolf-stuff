s=input()
num=""
if len(s)>2:
    num=len(s)-2
f, l = s[0], s[-1]
print(f+str(num)+l)