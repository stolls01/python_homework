from util import read_input
import re
lines = read_input("input_4.txt")

def matchsm(string):
    if bool(re.findall("S.M", string)) is True:
        return True

def matchms(string):
    if bool(re.findall("M.S", string)) is True:
        return True

def matchss(string):
    if bool(re.findall("S.S", string)) is True:
        return True

def matchmm(string):
    if bool(re.findall("M.M", string)) is True:
        return True

def matcha(string):
    if bool(re.findall(".A.", string)) is True:
        return True


count = 0

for y in range(len(lines)-2):
    for x in range(len(lines)-2):
        if matchms(lines[y][x:x+3]) is True and matcha(lines[y+1][x:x+3]) is True and matchms(lines[y+2][x:x+3]) is True:
            count += 1
        if matchsm(lines[y][x:x+3]) is True and matcha(lines[y+1][x:x+3]) is True and matchsm(lines[y+2][x:x+3]) is True:
            count += 1
        if matchss(lines[y][x:x+3]) is True and matcha(lines[y+1][x:x+3]) is True and matchmm(lines[y+2][x:x+3]) is True:
            count += 1
        if matchmm(lines[y][x:x+3]) is True and matcha(lines[y+1][x:x+3]) is True and matchss(lines[y+2][x:x+3]) is True:
            count += 1

print(count)