n=int(input())
c="*"
for i in range(0,n):
    print(c)
    c+="*"
for i in range(0,n):
    print(c)
    c=c[0:len(c)-1]
    n+=1
print(c)