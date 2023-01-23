def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            if isinstance(my_list[i], int):
                print(my_list[i], end=' ')
            i += 1
        print()
        return x
    except IndexError:
        while i < len(my_list):
            if isinstance(my_list[i], int):
                print(my_list[i], end=' ')
            i += 1
        print()
        return len(my_list)
