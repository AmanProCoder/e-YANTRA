def dec_to_binary(n):
    
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return int(n%2) + dec_to_binary(int(n/2))*10

# Main function
if __name__ == '__main__':
    

    test_cases = int(input())
    l=[]

    for case in range(1,test_cases+1):
        n = int(input())
        l.append(n)
    
    for i in l:
        bin_num = dec_to_binary(i)
        ad=str()
        length=(len(str(bin_num)))
        for j in range(8-length):
            ad=str(0)+ad
        print(ad+str(bin_num))