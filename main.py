import numpy as np
n = int(input("Введите количество элементов: "))
print("Введите элементы:")
a = np.zeros(n, dtype=int)
for i in range (n):
    a[i] = int(input())

for i in range(n - 1):
    for j in range(n - i - 1):
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
