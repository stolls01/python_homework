from util import read_input
import re
lines = read_input("input_3.txt")

# 1. read input
# 2. "splice" all lines
# 3. feed those into regex function to calculate all mul()s
# test = "don't()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()don't()?muldo()(8,5))"

def mul(a, b):
    return a * b

def find_mul(line):
    x = re.findall("mul[(][0-9]+,[0-9]+[)]", line)
    return(x)

def splice(line):
    cutline = ""
    status = True
    for x in range(len(line)):
        if line[x:x+7] == "don't()":
            status = False
        elif line[x:x+4] == "do()":
            status = True
        if status is True: cutline += line[x]
    return cutline

gigantic = ""
for line in lines:
    gigantic += line

multiply = []                                           # PART ONE
multiply.append(find_mul((gigantic)))

#multiply = []                                            PART TWO
#multiply.append(find_mul(splice(gigantic)))             

score = 0
for x in range(len(multiply)):
    for m in multiply[x]:
        score += eval(m)

print(score)