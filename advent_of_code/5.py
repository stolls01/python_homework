from util import read_input

lines = read_input("input_5.txt")

# divide input into instructions vs pages
instruction_pairs = []
updates = []
for line in lines:
    pair = []
    pages = []
    if "|" in line:
        lsp = line.split("|")
        pair.append(int(lsp[0]))
        pair.append(int(lsp[1]))
        instruction_pairs.append(pair)
    if "," in line:
        lsp = line.split(",")
        for l in lsp:
            pages.append(int(l))
        updates.append(pages)

def check_ordering(manual):
    status = True
    for x in range(len(manual)):
        smallerthan = []
        for z in instruction_pairs:
            if manual[x] == z[0]: smallerthan.append(z[1])
        for s in smallerthan:
            for t in manual[:x]:
                if s == t: status = False
    return status

correct_manuals = []
incorrect_manuals = []
for y in updates:
    if check_ordering(y) is True: correct_manuals.append(y)
    if check_ordering(y) is False: incorrect_manuals.append(y)


### PART ONE
correct_count = 0
for c in correct_manuals:
    middle = int((len(c)-1)/2)
    correct_count += c[middle]

print("Part 1:", correct_count)


### PART TWO
# go through every position in incorrect manual, check the numbers that its not allowed to occur after
# if the number occurs before it's supposed to: pop the number and insert it one position up
# rerun the reordering function until the manual is correctly ordered, return it and find middle value

def reorder(manual):
    for x in range(len(manual)):
        smallerthan = []
        for z in instruction_pairs:
            if manual[x] == z[0]: smallerthan.append(z[1])
        for t in range(len(manual[:x])):
            q = manual[t]
            for s in smallerthan:
                if s == q:
                    manual.pop(t)
                    manual.insert(t+1, q)
    return manual

def reorder_until_correct(serial):
    serial = reorder(serial)
    if check_ordering(serial) is True:
        return serial
    while check_ordering(serial) is False:
        serial = reorder(serial)
        if check_ordering(serial) is True:
            return serial

updated_manuals = []
for i in incorrect_manuals:
    updated_manuals.append(reorder_until_correct(i))

corrected_count = 0
for u in updated_manuals:
    middle = int((len(u)-1)/2)
    corrected_count += u[middle]

print("Part 2:", corrected_count)
