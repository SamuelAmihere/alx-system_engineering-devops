#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ac = len(sys.argv) - 1

    header = "{} argument{}".format(
            ac,
            ":" if ac == 1 else "s:" if ac > 0 else "s.")

    print("{}".format(header))

    if ac > 0:
        av = sys.argv[1:]
        for n, arg in enumerate(av):
            print("{}: {}".format(n + 1, av[n]))
