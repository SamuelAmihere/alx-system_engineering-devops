#!/usr/bin/python3
"""A module that computes metrics
by reading from standard input.

Prints the following metrics after every ten lines or the
input of a keyboard interruption (CTRL + C):
    Total file size up to that point.
    Total Count of read status codes up to that point.
"""


def print_metrics(total_file_size, status_counts):
    """Prints metrics from the given data."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403',
                   '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_metrics(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.strip().split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    status_codes[line[-2]] =\
                        status_codes.get(line[-2], 0) + 1
            except IndexError:
                pass

        print_metrics(size, status_codes)

    except KeyboardInterrupt:
        print_metrics(size, status_codes)
        raise
