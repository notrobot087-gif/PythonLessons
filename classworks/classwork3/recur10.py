def digit_sum(k):
    if k<10:
        return k
    return (k%10)+digit_sum(k//10)

for i in range(5):
    a=int(input("number:"))
    print(digit_sum(a))