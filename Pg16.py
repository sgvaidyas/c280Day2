number = int(input('input number\n'))
rotations = int(input('input number of rotations\n'))
while rotations>0:
        tempNum = number
        count = 0
        while tempNum!=0:
            tempNum//=10
            count +=1
        rightdig= number%10
        leftnum= number // 10
        newNumber = leftnum+rightdig*10**(count-1)
        print("rightshift of {} = {}".format(number, newNumber))
        number = newNumber
        rotations-=1
