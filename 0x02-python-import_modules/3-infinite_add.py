#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    argc = len(sys.argv) - 1
    for i in range(1, argc + 1):
        result += int(sys.argv[i])
    print("{}".format(result))
