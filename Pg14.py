n = 7

for row in range(1, n + 1):
    for col in range(n + 1 - int(not n%2)):
        if (col + row > n - 0 - int(not n%2) and col - row >= -0 - int(not n%2)) or (col + row < n + 1 and col - row <= -1):
            print("*", end="\t")
        else:
            print("", end="\t")
    print("")
