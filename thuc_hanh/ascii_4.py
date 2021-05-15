def ascii(a):
    for i in a:
        print(ord(i), end='')


def main():
    n = list(input("nhập chuỗi: "))
    ascii(n)


if __name__ == '__main__':
    main()
