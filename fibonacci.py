n=int(input())
if n==0:
    print(0)
elif n==1:
    print(0)
else:
    pn=0
    q=1
    for i in range(2, n+1):
        nn=pn+q
        pn=q
        q=nn
    print(q)