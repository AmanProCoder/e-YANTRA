t=int(input())
l=[]
for i in range(t):
    a=list(map(int,input().split()))
    l.append(a)
for i in l:
    print("%0.2f"%((i[0]-i[1])**2+(i[2]-i[3]**2)))

    
