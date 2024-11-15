from func import *


h = input("what reverse value you want?")
i = input("string or list?")
if i == "list":
    print(reverse_list(h.split(",")))
elif i == "string":
    print(reverse_string(h))
