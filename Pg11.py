n = int(input("Enter the number:"))

for row in range(1, n+1):
    for col in range(n):
        if col+row > n-1 and col-row >= -1:
            print("*", end="\t")
        elif col+row < n+1 and col-row <= -1:
            print("*", end="\t")
        else:
            print("", end="\t")
    print("")
