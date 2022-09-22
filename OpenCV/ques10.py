t=int(input())
l={}
my=[]
for i in range(t):
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
                print("ADDED Item",l1[1])
            else:
                b=int(l[l1[1]])
                c=int(l1[2])
                a=b+c
                l[l1[1]]=str(a)
                print("UPDATED Item",l1[1])
        if(s.startswith("DELETE")):
            l1=s.split()
         
            if(l1[1] not in l):
                print("Item",l1[1],"does not exist")
            else:
                b=int(l[l1[1]])
                c=int(l1[2])
                if(b>c):
                    a=b-c
                    l[l1[1]]=str(a)
                    print("DELETED Item",l1[1])
                else:
                    print("Item",l1[1],"could not be DELETED")
  
x=l.values()
c=0
for i in x:
    c=c+int(i)
    
print("total items in inventory:",c)
                

