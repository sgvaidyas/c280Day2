import math
n = int(input("Please enter a number    -> "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row < math.ceil(n/2)+1 and col <= row:
            print("*", end="\t")
        elif row > n/2 and col >= row:
            #math.ceil(n / 2)-1
            print("*", end="\t")
        else:
            print("\t", end="")
    print()
