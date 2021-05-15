def f(a):
    a = []
    for i in range(5):
        i = i ** 3
        a.append(i)
    yield a
    # return a


def main():
    for x in f(5):
        print(x,)


if __name__ == '__main__':
    main()
