n = int(input("Enter the number  = "))
r = int(input("Enter the no of rotations  = "))
while r>0:
    temp = n
    cnt = 0
    while temp!=0:
        temp //= 10
        cnt += 1
    leftdig = n // 10**(cnt-1)
    rightnum = n % 10**(cnt-1)
    newnum = rightnum*10 + leftdig
    print("Leftshift of {} = {}".format(n,newnum))
    n = newnum
    r-=1
