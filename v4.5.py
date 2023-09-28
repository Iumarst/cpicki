import random
ymca = []

for i in range(10):
        ymca.append(random.randint(0, 100))
print(ymca)

r = 0
f = 1

for i in ymca:
        r += i
        f *= i

print(r)
print(f)