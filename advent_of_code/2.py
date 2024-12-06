from util import read_input
lines = read_input("input_2.txt")

# are numbers ascending or descending in order
def in_order(line):
    line2 = sorted(line)
    if line == line2 or line == line2[::-1]:
        return True

# are all differences between neighboring numbers between 1 and 3
def diff_in_range(line):
    tf = ""
    for x in range(len(line)-1):
        diff = abs(line[x] - line[x+1])
        if diff > 3 or diff == 0:
            tf += "STOP"
    if "STOP" not in tf:
        return True

# see if sequence is safe
def safe_sequence(line):
    if in_order(line) is True and diff_in_range(line) is True:
        return True

# get all permutations of a sequence, popping one element each
def variations(seq):
    popped = {}
    for x in range(len(seq)):
        popped[x] = []
        for y in seq[:x]:
            popped[x].append(y)
        for y in seq[x+1::]:
            popped[x].append(y)
    return(list(popped.values()))

# get all lines into object
all = []
for line in lines:
    temp = []
    for s in line.split():
        temp.append(int(s))
    all.append(temp)

safe_seqs = 0                               # PART ONE
for line in all:        
    if safe_sequence(line) is True:
        safe_seqs += 1                     
print("Part 1:", safe_seqs)

safe_seqs = 0                               # PART TWO
for line in all:
    if safe_sequence(line) is True:
        safe_seqs += 1
    else:
        temp = ""
        for v in variations(line):
# variations(line = [[30, 29, 28, 26, 24, 24], [37, 29, 28, 26, 24, 24], [37, 30, 28, 26, 24, 24], [37, 30, 29, 26, 24, 24],
# [37, 30, 29, 28, 24, 24], [37, 30, 29, 28, 26, 24], [37, 30, 29, 28, 26, 24]]
            if safe_sequence(v) is True:
                temp += "nice"
        if "nice" in temp:
            safe_seqs += 1

print("Part 2:", safe_seqs)