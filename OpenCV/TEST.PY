from math import dist

def compute_distance(x1, y1, x2, y2):
    # distance = "%0.2f"%(math.sqrt(((x1-x2)**2+(y1-y2)**2)))
    p=[x1,y1]
    q=[x2,y2]
    distance=dist(p,q)
    return distance
    

    

if __name__ == '__main__':
    l=[]
    test_cases = int(input())
    for i in range(test_cases):
        a=list(map(int,input().split()))
        l.append(a)
    for i in l:
        x1=i[0]
        y1=i[1]
        x2=i[2]
        y2=i[3]
        print(compute_distance(x1, y1, x2, y2))