#!/usr/bin/env python3

import sequences as sq

def main(argv):
    print (sq.fibonacci(int(argv[1]))[int(int(argv[1])-1)])
if __name__ == "__main__":
    import sys
    main(sys.argv)
