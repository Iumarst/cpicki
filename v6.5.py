import random

rgn = []

for i in range(10):
        rgn.append(random.randint(0, 10))

print(rgn)

for i in rgn:
        if rgn.count(i) > 1:
            print(i)