def nod(A, B):
  if B == 0:
    return A
  return nod(B, A % B)
x = int(input("a"))
y = int(input("b"))
z = int(input("c"))
w = int(input("d"))
print(nod(x, y))
print(nod(x, z))
print(nod(x, w))