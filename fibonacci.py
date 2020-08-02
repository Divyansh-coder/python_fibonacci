def fb(n):
    """fb function is defined which return a list of fibonacci series"""
    fibonacci=[0,1]
    for i in range(n-2):
        num=fibonacci[i]+fibonacci[i+1]
        fibonacci.append(num)
    return fibonacci
n=int(input("Length of Fibonacci seres to be printed: "))
result=fb(n)
#print fibonacci series in a line
for t in result:
    print(t,end=" ")
