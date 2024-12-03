from util import read_input
import re
lines = read_input("input_3.txt")

#correct (niko) would be:       100189366
#i get which is FALSE:          101681733

# 1. read input
# 2. "splice" all lines
# 3. feed those into regex function from part 1 to calculate all mul()s
# test = "don't()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()don't()?muldo()(8,5))"

def mul(a, b):
    return a * b

def find_mul(line):
    x = re.findall("mul[(][0-9]+,[0-9]+[)]", line)
    return(x)

# issue must be here somewhere since its only part different from part 1 which works
def splice(line):
    cutline = ""
    status = True
    for x in range(len(line)):
        if line[x:x+7] == "don't()":
            status = False
        elif line[x:x+4] == "do()" or bool(status) is True:
            status = True
            cutline += line[x]
    return cutline

# PART ONE
#multiply = []
#for line in lines:
#    multiply.append(find_mul((line)))

multiply = []
for line in lines:
    multiply.append(find_mul(splice(line)))

score = 0
for x in range(len(multiply)):
    for m in multiply[x]:
        score += eval(m)

print(score)


def splice(line):
    cutline = ""
    status = True
    for x in range(len(line)):
        if line[x:x+7] == "don't()":
            status = False
        elif line[x:x+4] == "do()" or bool(status) is True:
            status = True
            cutline += line[x]
    return cutline