import random

r = int(input("Введите число - "))
p = [random.randint(0, 25) for _ in range(10)]

print(p)

if r in p:
    print(p.index(r))
else:
    print('-1')