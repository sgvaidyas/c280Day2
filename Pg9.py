n = int(input("Enter the number:"))
row = 2*n
col = (4*n) - 2
for r in range(1,row+1):
    for c in range(1,col+1):
        if r+c == n+1 or c-r == n-1 or r+c==(5*n)-1:
            print("*\t",end="")
        else:
            print(" \t",end="")
    print()
