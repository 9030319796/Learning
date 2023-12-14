def fibonacci(n):
    fib_series = [0,1]

    if n <= 0:
        print("Please enter the postive number..!")
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_series

    for i in range(2,n):
        numseries = fib_series[i-1] + fib_series[i-2]
        fib_series.append(numseries)

    return fib_series

n_term = 15

print(fibonacci(n_term))


# second method

n_term = 15
n1 = 0
n2 = 1
n3 = n2
count = 1
while count <= n_term:
    print(n3,end=" ")
    count += 1
    n1,n2 = n2,n3
    n3 = n1+n2
print()    

       

