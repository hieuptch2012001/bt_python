def number():
    a = []
    for i in range(101):
        a.append(i)

    return a


def main():
    lst = number()
    for i in lst:
        print(i, end="")


if __name__ == '__main__':
    main()
