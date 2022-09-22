t=int(input())
store=[]
for i in range(t):
    a=int(input())
    l=list(map(int,input().split()))
    store.append(l)
for l in store:
    for i in l[-1::-1]:
        print(i,end=" ")
    print()
    for i in l[3::3]:
        print(i+3,end=" ")
    print()
    for i in l[5::5]:
        print(i-7,end=" ")
    sum=0
    for i in l[3:8]:
        sum=sum+i
    print("\n"+str(sum))