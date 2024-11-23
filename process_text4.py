"""
the 4th version of the process_text function (replace).
"""
from functions import *


i = input("text")
f = input("what replace/count")
print("if you don't want to replace anything write 'do not replace'")
rrt = input("for what replace")
rrr = '\033[91m' + f + '\033[0m'
rtr = process_text(i, f)
if rtr is not None:
    r1 = replace_text(i, f, rrr)
    r2 = replace_text(i, f, rrt)
    print(len(rtr))
    print(r1)
    if not rrt == "do not replace":
        print(r2)
else:
    print(f + " do not found")
