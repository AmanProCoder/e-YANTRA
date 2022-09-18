t=int(input())
l=[]
for i in range(t):
    a=str(input())
    a=a.lower()
    l.append(a)
for i in l:
    b = "".join(reversed(str(i))) 
    if(i==b):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")