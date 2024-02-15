#!/usr/bin/python3
for n, asc in enumerate(reversed(range(97, 123))):
    print("{}".format(chr(asc) if n % 2 == 0 else chr(asc - 32)), end="")
