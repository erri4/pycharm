from functions import *


i = input("number")

if isnumber(i):
    if is_prime(i) == bool(1):
        print(str(i) + " is prime ")
    else:
        print(str(i) + " is not prime ")

    for a in range(abs(int(i))-1, 1, -1):
        g = is_prime(a)
        if g == bool(1):
            print(f'{str(a)} is the largest prime number less than {str(i)}')
            break
