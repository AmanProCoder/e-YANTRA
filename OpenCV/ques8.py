# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):

    AP_series = []

    # Complete this function to return A.P. series
    for i in range(n):
        AP_series.append(a1)
        a1=a1+d

    return AP_series


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())
    l=[]
    AP_series=[]
    sqr_AP_series =[]
    sum_sqr_AP_series  =[]
    # Write the code here to take the a1, d and n values
    for i in range(test_cases):
        d=list(map(int,input().split()))
        l.append(d)
    for i in range(test_cases):
        # Once you have all 3 values, call the generate_AP function to find A.P. series and print it
        AP_series.append( generate_AP(l[i][0], l[i][1], l[i][2]))
    for i in range(test_cases):
        # Using lambda and map functions, find squares of terms in AP series and print it
        sqr_AP_series.append(list(map(lambda x:x**2,AP_series[i])))
    for i in range(test_cases):
        # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
        sum_sqr_AP_series.append(reduce(lambda x,y:x+y,sqr_AP_series[i]))
    for i in range(test_cases):
        for j in AP_series[i]:
            print(j,end=" ")
        print()
        for j in sqr_AP_series[i]:
            print(j,end=" ")
        print()
        print(sum_sqr_AP_series[i])
        