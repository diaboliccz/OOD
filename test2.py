def fibo(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibo(n-1)
        return (a+b, a)
print(fibo(10)[0])