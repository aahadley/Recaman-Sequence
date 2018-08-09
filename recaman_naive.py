# For Testing:
# Naive solution for generating the Recamann sequence
# Put numbers into a dict as they are generated

import sys

def main(end):

    n = 0
    database = {}

    while jump < end:

        key = n - jump

        if key in database or key < 0:
            n = n + jump
        
        else:
            n = key

        print(n, "\t\t\t\t", jump + 1)
        database[n] = True
        jump = jump + 1


if __name__ == "__main__":
    main(int(sys.argv[1]))