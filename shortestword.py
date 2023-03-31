i=input()
i=i.split()
s=i[0]
for j in i:
    if len(j)<len(s):
        s=j
print(s)