r = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
d = []

for i in r:
        if i in r and i in p:
            d.append(i)

print(d)