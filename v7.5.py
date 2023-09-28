import random
lmg = []
for i in range(10):

        lmg.append(random.randint(0, 100))

x = lmg.copy()

maximum = lmg.index(max(lmg))

minimum = lmg.index(min(lmg))

x[maximum] = min(lmg)


x[minimum] = max(lmg)

print(lmg)
print(x)