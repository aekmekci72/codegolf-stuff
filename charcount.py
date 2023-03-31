s=input()
s=s.split(", ")
c=s[1]
s=s[0]
s=[z for z in s]
f=0
for t in s:
    if c==t:
        f+=1
print(f)