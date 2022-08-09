n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
if n % 2 == 0:
    len = int(n / 2)
else:
    len = int(n / 2) + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if len > i >= j or (i == len and j<=len and n%2==0) or (i == len and  n%2==1):
            print("*\t", end="")
        elif i > len:
            if len % 2 == 0 and j >= i:
                print("*\t", end="")
            elif len % 2 != 0 and j >= i:
                print("*\t", end="")
            else:
                print(" \t", end="")
    print()
