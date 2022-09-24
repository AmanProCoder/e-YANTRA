t=int(input())
ans=[]
for i in range(t):
    l={}
    my=[]
    m=int(input())
    for j in range(m):
        s=input()
        l1=s.split()
        l[l1[0]]=l1[1]
    m=int(input())
    for k in range(m):
        s=input()
        my.append(s)
    for z in my:
        s=z
        if(s.startswith("ADD")):
            l1=s.split()
          
            if(l1[1] not in l):
                l[l1[1]]=l1[2]
                mystr="ADDED Item "+str(l1[1])
                ans.append(mystr)
            else:
                b=int(l[l1[1]])
                c=int(l1[2])
                a=b+c
                l[l1[1]]=str(a)
                mystr="UPDATED Item "+str(l1[1])
                ans.append(mystr)

        if(s.startswith("DELETE")):
            l1=s.split()
            if(l1[1] not in l):
                mystr="Item "+l1[1]+" does not exist"
                ans.append(mystr)

            else:
                b=int(l[l1[1]])
                c=int(l1[2])
                if(b>c):
                    a=b-c
                    l[l1[1]]=str(a)
                    mystr="DELETED Item "+str(l1[1])
                    ans.append(mystr)

                else:
                    mystr="Item "+str(l1[1])+" could not be DELETED"
                    ans.append(mystr)
    x=l.values()
    c=0
    for i in x:
        c=c+int(i)
    mystr="Total Items in Inventory: "+str(c)
    ans.append(mystr)

for i in ans:
    print(i)
                

