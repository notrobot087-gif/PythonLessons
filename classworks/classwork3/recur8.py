def RootK(x, k, n):
    if n == 0:
        return 1.0
    prev = RootK(x, k, n - 1)
    return prev - (prev - x / (prev ** (k - 1))) / k

x = float(input("Введите X: "))
k = int(input("Введите K: "))
for i in range(6):
    n = int(input("N: "))
    print(RootK(x, k, n))
