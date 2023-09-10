n = int(input())

for i in range(n + 1):
    ms = []
    for j in range(1,10):
        if i % (n / j) == 0:
            ms.append(j)
    if ms:
        print(min(ms), end="")
    else:
        print("-", end="")
print()