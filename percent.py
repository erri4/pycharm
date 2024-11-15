from func import *

while 1 == 1:
    f = input("percent from what:")
    if isnumber(f) == bool(0) and f == "exit":
        break
    elif isnumber(f) == bool(1):
        y = int(f)
        p = input("percent:")
        if isnumber(p) == bool(0) and p == "exit":
            break
        elif isnumber(p) == bool(1):
            x = int(p)
            my = y / 100 * x
            print(my)
