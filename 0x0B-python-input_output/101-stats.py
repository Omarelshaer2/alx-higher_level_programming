#!/usr/bin/python3

import sys

status_codes = {
    '200': 0,  # Capture count of occurrences where HTTP 200 status received
    '301': 0,  # Capture count of occurrences where HTTP 200 status received
    '400': 0,  # Capture count of occurrences where HTTP 200 status received
    '401': 0,  # Capture count of occurrences where HTTP 200 status received
    '403': 0,  # Capture count of occurrences where HTTP 200 status received
    '404': 0,  # Capture count of occurrences where HTTP 200 status received
    '405': 0,  # Capture count of occurrences where HTTP 200 status received
    '500': 0   # Capture count of occurrences where HTTP 200 status received
}

lc = 0  # Line counter
file_size = 0  # Total file size counter


def print_info():
    """
    Print file size and status code occurrences
    """
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_info()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except Exception:
            pass

        try:
            file_size += int(pieces[-1])
        except Exception:
            pass

        lc += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
    
