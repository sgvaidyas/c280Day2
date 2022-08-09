n = int(input("Please enter a number    > "))
for i in range(n):
    if i % 2 ==0:
        for x in range(1,n-i+1):
            print(x, end="\t")
    else:
        for x in range(n-i, 0,-1):
            print(x, end="\t")
    print()
