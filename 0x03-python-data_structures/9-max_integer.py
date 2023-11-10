#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    max_val = my_list[0]
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))

