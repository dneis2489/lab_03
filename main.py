import numpy as np
direction = input("Введите направление сориторки, где up - по возрастанию (от меньшего к большему)"
                  ", down - по убыванию (от большего к меньшему): ")
n = int(input("Введите количество элементов: "))
print("Введите элементы:")
a = np.zeros(n, dtype=int)
for i in range (n):
    a[i] = int(input())

for i in range(n - 1):
    for j in range(n - i - 1):
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

if (direction == 'up'):
    print(a)
else:
    print(np.flip(a))
