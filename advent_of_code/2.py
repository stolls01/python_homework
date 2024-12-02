from util import read_input

filepath = "input_2.txt"
lines = read_input(filepath)

# are numbers ascending in order
def ascending(line):
    line2 = sorted(line)
    if line == line2:
        return True

#are they descending in order
def descending(line):
    line2 = sorted(line)
    if line == line2[::-1]:
        return True

# are all differences between neighboring numbers between 1 and 3
def diff_in_range(line):
    temp = []
    tf = ""
    for x in range(len(line)-1):
        temp.append(abs(line[x] - line[x+1]))
    for x in temp:
        if x > 3 or x == 0:
            tf += "STOP"
    if "STOP" in tf:
        return False
    else:
        return True

# see if sequence is safe
def safe_sequence(line):
    if ascending(line) is True or descending(line) is True:
        if diff_in_range(line) is True:
            return True

# get all variations of a sequence, popping one element each
def variations(seq):
    popped = {}
    for x in range(len(seq)):
        popped[x] = []
        for y in seq[:x]:
            popped[x].append(y)
        for y in seq[x+1::]:
            popped[x].append(y)
    return(list(popped.values()))

########################################################################

# get all lines into object
all = []
for line in lines:
    temp = []
    splitline = [int(x) for x in line.split()]
    for s in splitline:
        temp.append(s)
    all.append(temp)


############ PART ONE
#safe_seqs = 0
#for line in all:
#    if safe_sequence(line) is True:
#        safe_seqs += 1
#print(safe_seqs)

############ PART TWO
safe_seqs = 0
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

print(safe_seqs)