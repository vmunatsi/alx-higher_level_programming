#!/usr/bin/python3
for i in range(100):
    if (i != 99):
        print("{:d}{}".format(int(i / 10), int(i % 10)), end=", ")
    else:
        print("{:d}{}".format(int(i / 10), int(i % 10)))
