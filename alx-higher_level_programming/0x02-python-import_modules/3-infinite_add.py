#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    av = sys.argv[1:]

    print("{}".format(sum([int(i) for i in av]) if len(av) > 0 else 0))
