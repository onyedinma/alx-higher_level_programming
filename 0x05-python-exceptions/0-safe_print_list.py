#!/usr/bin/python3
# 0-safe_print_list.py
# Onyedinma Onyekachi <onyedinmaonyekachi@gmail.com>

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print(my_list[i], end=' ')
            i += 1
        print()
        return x
    except IndexError:
        while i < len(my_list):
            print(my_list[i], end=' ')
            i += 1
        print()
        return len(my_list)


