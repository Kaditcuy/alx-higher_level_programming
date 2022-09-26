#!/usr/bin/python3
def no_c(my_string):
    output = ''
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        output += my_string[i]

    return output
