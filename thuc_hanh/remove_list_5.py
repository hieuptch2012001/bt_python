def remove(a):
    while("" in a):
        a.remove("")

    print("modified list is: " + str(a))


def main():
    n = ["", "hehe", "lolo", "", 1]
    remove(n)


if __name__ == "__main__":
    main()

# c2:
# a = [i for i in a if i]

# c3:
# a = list(filter(None, a))
