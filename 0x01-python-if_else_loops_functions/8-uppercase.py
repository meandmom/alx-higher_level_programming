#!/usr/bin/python3
def uppercase(str):
    x = ''
    for a in str:
        b = ord(a)
        if b >= 32 & b <= 122:
            if 32 <= b < 65:
                x += a
            elif 65 <= b <= 90:
                x += chr(b)
            else:
                x += chr(b - 32)
    print("{}".format(x))
