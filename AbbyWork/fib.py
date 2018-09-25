#!/usr/bin/env python3

# Royal Cuevas and Abigail Wheaton
# 2285562 and 2299246
# cueva114@mail.chapman.edu and wheaton@chapman.edu
# PHYS220 Fall 2018
# CW 03

import sequences

def main(argv):
    print( sequences.fibonacci(int(argv[1]))[int(int(argv[1])-1)])

if __name__ == "__main__":
    import sys
    main(sys.argv)
