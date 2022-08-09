def checkDigit(num,digit):
    while num>0:
        rem = num%10
        if digit==rem:
            return True
        num //=10
    return False

number = int(input("Enter the number = "))
digit = int(input("Enter a digit = "))
print(checkDigit(number,digit))
