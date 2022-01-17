#!/usr/bin/python3
from multiprocessing.sharedctypes import Value


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError):
            continue
    print()
    return count
