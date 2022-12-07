#!/usr/bin/python3
def no_c(my_string):
    my_new_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            my_new_str += char
    return (my_new_str)
