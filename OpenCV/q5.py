t=int(input())
l=[]
for i in range(t):
    a=str(input())
    l.append(a)
for i in l:
    c=int(0)
    b=True
    length=len(i)
    iter=int(0)
    for j in i:
        iter=iter+1
        if(j=='@'):
            continue
        elif(j==" "):
            if(b):
                print(str(c),end="")
                b=False
            else:
                print(","+str(c),end="")
            c=int(0)
        elif(iter==length):
            print(","+str(c+1),end="")
        else:
            c=c+1
    print()

