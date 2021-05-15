def unique(a):
    setlst = set(a)
    print(list(setlst))


def main():
    n = input().split(",")
    unique(n)


if __name__ == '__main__':
    main()
