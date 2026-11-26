f_count=0

def fib(n,saves=None):
    global f_count
    f_count+=1
    if saves == None:
        saves = {

        }
    if n==1 or n==2:
        return 1
    if n in saves:
        return saves[n]
    a = fib(n-2,saves)
    b = fib(n-1,saves)
    saves[n]=a+b
    return saves[n]

a=int(input())
print(fib(a))
print(f_count)