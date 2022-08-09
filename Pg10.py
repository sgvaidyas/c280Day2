n = int(input("Enter the number:"))
mid = n/2 + 0.5
for r in range(1,n+1):
    for c in range(1,n+1):
        if r+c <=mid or c-r >= mid or r - c >= mid or r+c >=mid*3:
            print("* ",end="")
        else:
            print("- ",end="")
    print()
