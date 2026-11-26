f_count=0

def fib(n):
    global f_count
    f_count+=1
    if n==1 or n==2:
        return 1

    a=fib(n-2)
    b=fib(n-1)
    return a+b
a=int(input())
print(fib(a))
print(f_count)