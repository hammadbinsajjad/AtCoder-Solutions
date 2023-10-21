def main():
    n = int(input())

    for i in range(61):
        for j in range(40):
            if (2**i * 3**j) == n:
                print("Yes")
                return
    print("No")
main()