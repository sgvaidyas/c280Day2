def task12():
    inp = int(input("Choose a number:\n"))
    for i in range(1, inp + 1):
        if inp % 2 == 1:
            gap1 = (inp+1-2*i)
            gap2 = (inp+1 - 2 * (inp-i+1))
        else:
            gap1 = (inp-2*i)
            gap2 = (inp - 2 * (inp - i)-2)
        if i <= inp/2:
            pattern = i * "*"
            pattern += gap1 * " "
            pattern += i * "*"
        else:
            pattern = (inp-i+1) * "*"
            pattern += gap2 * " "
            pattern += (inp-i+1) * "*"
        print(pattern)

if __name__ == '__main__':
    task12()
