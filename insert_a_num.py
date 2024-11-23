from functions import *


num_loop = 0
while num_loop < 5:
    num_loop += 1
    o = ""
    num = input('Insert a number : ')
    if isnumber(num) or num == "exit" or num == "=":
        while not num == "exit":
            if not num == "=" and not num == "":
                if isnumber(num):
                    num1 = int(num)
                    o += (str(num1)) + " "
            num = input('Insert a number : ')
            if num == "=" and is_zero(o, " ") == bool(0):
                print(sam(num_string(o), num_sum(o)))
            if num == "exit":
                break
        break
