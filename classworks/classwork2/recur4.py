def fib(n):
    if n==1 or n==2:
        return 1

    a=fib(n-2)
    b=fib(n-1)
    return a+b
a=int(input())
print(fib(a))