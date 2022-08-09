import math
n = int(input("Please enter a number    -> "))
mid = math.ceil(n/2)
for row in range(1,n+1):
    for col in range(1,n+1):
        if col<=row and row<=mid:
            print("*\t",end="")
        elif col>=row and row>n/2:
            print("*\t",end="")
        else:
            print(" \t",end="")

    print()
