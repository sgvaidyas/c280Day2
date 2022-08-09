def task9():
    inp = int(input("Choose a number:\n"))
    pattern = ""

    for i in range(1, inp + 1):
        if i <= inp/2 :
            pattern += "* "
        elif i == int((inp+1)/2) and inp%2==1:
            pattern =  inp*"* "
        else:
            pattern=""
            pattern += (i-1)*"  "
            pattern += (inp-i+1)*"* "
        print(pattern)

if __name__ == '__main__':
    task9()
