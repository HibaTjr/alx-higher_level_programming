#!/usr/bin/env python3

def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char not in "cC":
            new_string += char
    return new_string

if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))

