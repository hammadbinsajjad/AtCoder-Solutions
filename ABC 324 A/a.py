n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    if a[i] == a[i - 1]:
        continue
    else:
        print("No")
        import sys
        sys.exit(0)
print("Yes")