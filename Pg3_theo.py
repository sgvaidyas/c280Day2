def task7():
    inp = int(input("Choose a number:\n"))
    offset = 0
    for i in range(1, inp + 1):
        if i % 2 == 1:
            for k in range(1, inp + 1 - offset):
                print(k, end=" ")
        else:
            for k in range(inp - offset, 0, -1):
                print(k, end=" ")
        offset += 1
        print("")


if __name__ == '__main__':
    task7()
