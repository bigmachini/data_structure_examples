import math
import os
import random
import re
import sys

input_re = '[a-z]{1,20}\\s[a-z]+@gmail.com'
name_re = '[a-z]{1,20}\\s'

if __name__ == '__main__':
    N = int(input())
    names = [
        'riya riya@gmail.com'
,'julia julia@julia.me'
,'julia sjulia@gmail.com'
,'julia julia@gmail.com'
,'samantha samantha@gmail.com'
,'tanya tanya@gmail.com'
,'riya ariya@gmail.com'
,'julia bjulia@julia.me'
,'julia csjulia@gmail.com'
,'julia djulia@gmail.com'
,'samantha esamantha@gmail.com'
,'tanya ftanya@gmail.com'
,'riya riya@live.com'
,'julia julia@live.com'
,'julia sjulia@live.com'
,'julia julia@live.com'
,'samantha samantha@live.com'
,'tanya tanya@live.com'
,'riya ariya@live.com'
,'julia bjulia@live.com'
,'julia csjulia@live.com'
,'julia djulia@live.com'
,'samantha esamantha@live.com'
,'tanya ftanya@live.com'
,'riya gmail@riya.com'
,'priya priya@gmail.com'
,'preeti preeti@gmail.com'
,'alice alice@alicegmail.com'
,'alice alice@gmail.com'
,'alice gmail.alice@gmail.com']

    test = []

    for N_itr in names:
        firstNameEmailID = N_itr
        p =  re.compile(input_re)
        x = re.compile(name_re)
        if p.match(firstNameEmailID) and x.match(firstNameEmailID):
            data = x.match(firstNameEmailID).group()
            if data:
                test.append(data)
    
    test = sorted(test)
    for name in test:
        print (name)