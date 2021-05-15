def binary(a):
    decimal = 0
    for i in a:
        decimal = decimal * 2 + int(i)
    print(decimal)


def main():
    n = input("nhập số nhị phân: ")
    binary(n)


if __name__ == '__main__':
    main()
