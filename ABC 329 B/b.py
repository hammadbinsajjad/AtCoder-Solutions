n = int(input())

a = list(set(map(int, input().split())))

a.remove(max(a))

print(max(a))