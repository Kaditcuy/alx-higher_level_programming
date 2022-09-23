#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length <= 1:
        print("0 arguments.")
    elif length == 2:
        print('1: {}'.format(argv[1]))
    else:
        print('{:d} arguments:'.format(length - 1))
        for i in range(1, length):
            print('{:d}: {:s}'.format(i, argv[i]))
            i += 1