d={}
t=int(input())
name=[]
for i in range(t):
    m=int(input())
    for j in range(m):
        s=input()
        l=s.split()
        d[l[0]]=l[1]
    key=max(d.values())
    for n,k in d.items():
        if(k==key):
            name.append(n)
    name.sort()
    for j in name:
        print(j)



