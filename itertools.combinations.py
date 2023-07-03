from itertools import combinations

a = input().split()

for i in range(1, int(a[1]) + 1):
    x = a[0].upper()
    for j in combinations(sorted(x), i):
        print(''.join(j))