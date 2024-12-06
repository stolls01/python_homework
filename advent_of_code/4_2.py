from util import read_input
import re
lines = read_input("input_4.txt")

def matchsm(string):
    if bool(re.findall("S.M", string)) is True: return True

def matchms(string):
    if bool(re.findall("M.S", string)) is True: return True

def matchss(string):
    if bool(re.findall("S.S", string)) is True: return True

def matchmm(string):
    if bool(re.findall("M.M", string)) is True: return True

def matcha(string):
    if bool(re.findall(".A.", string)) is True: return True


count = 0

for y in range(len(lines)-2):
    for x in range(len(lines)-2):
        # creates sliding frame of 3x3 through slicing
        # feeds slice into match function and if conditions or x-mas are fulfilled, adds to count
        a = lines[y][x:x+3]
        b = lines[y+1][x:x+3]
        c = lines[y+2][x:x+3]
        if  (matchms(a) is True and matcha(b) is True and matchms(c) is True) or\
            (matchsm(a) is True and matcha(b) is True and matchsm(c) is True) or\
            (matchss(a) is True and matcha(b) is True and matchmm(c) is True) or\
            (matchmm(a) is True and matcha(b) is True and matchss(c) is True):
            count += 1

print("Part 2:", count)