#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num = len(sys.argv)
    sum = 0
    for i in range(1, num):
        sum += int(sys.argv[i])
    print("{}".format(sum))
