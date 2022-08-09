n = int(input("Enter the number:"))
if n%2 == 0:
    mid = (n/2)
else:
    mid = (n / 2) + 0.5

for row in range(1, n+1):
    for col in range(1,n+2):
        if (row+col <=n+1 and col<=row) or  (row+col>n+1 and row<=mid) or (col>row and row>mid):
            print("*\t",end="")
        elif col==mid+1 and n%2==0:
            continue
        else:
            print(" \t",end="")
    print()
