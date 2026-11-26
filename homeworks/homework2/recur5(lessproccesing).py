def fib(n,saves=None):
    if saves == None:
        saves = {

        }
    if n==1 or n==2:
        return 1
    a = fib(n-2,saves)
    b = fib(n-1,saves)
    saves[n]=a+b
    return saves[n]

a=int(input())
print(fib(a))