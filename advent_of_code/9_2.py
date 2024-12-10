from util import read_input
import copy


lines = read_input("input_9.txt")
input = ""
for line in lines:
    input += line
input = "2333133121414131402"

files = []
for x in range(0, len(input), 2):
    files.append(input[x])

free_spaces = []
for x in range(1, len(input), 2):
    free_spaces.append(input[x])

orig_block = []
for x in range(int((len(input)/2)+1)):
    temp = []
    if x in range(len(files)):
        for z in range(int(files[x])):
            orig_block.append(str(x))
    if x in range(len(free_spaces)):
        for z in range(int(free_spaces[x])):
            orig_block.append(".")

print("".join(orig_block))
block = copy.deepcopy(orig_block)
#print("".join(orig_block))
## 00...111...2...333.44.5555.6666.777.888899
#print("".join(block_flipped))
# 998888.777.6666.5555.44.333...2...111...00

# go through the block, for each number block, get start and finish index, put them together into object in numberblocks list
numberblocks = []
for num, x in enumerate(block, start = 0):
    status = False
    if x == ".":
        continue
    if x != "." and status is False:
        for y in range(10):
            if num+y < len(block) and (num + y + 1 == len(block) or block[num + y] != x) and status is False:
                filestart = num
                fileend = num + y
                if num + y + 1 == len(block):
                    fileend = len(block)
                if fileend not in [b[1] for b in numberblocks]:
                    numberblocks.append([filestart, fileend])
                status = True

# for n in numberblocks:
#     print(block[n[0]:n[1]])

# function to check if certain frame consists only of dots
def is_dots(dot, frame):
    temp = ""
    for f in frame:
        if f != dot: temp += "STOP"
    if bool(temp) is False: return True

# move number blocks all together into first open free space
def move(indices, block2):
    status = True
    block_length = indices[1]-indices[0]
    for num, x in enumerate(block2[:indices[0]], start = 0):
        frame = block2[num:num+block_length]
        # check if the sliding frame (exactly as long as the number block) contains only free spaces
        # if yes, takes the first instance
        if status and is_dots(".", frame) and num+block_length < len(block):
            dotties = block2[num:num+block_length]
            dots = copy.deepcopy(dotties)
            block2[num:num+block_length] = block2[indices[0]:indices[1]]
            block2[indices[0]:indices[1]] = dots
            status = False
        # if not, just go to next iteration
        # else, set status to false so that loop skips to next index
    return block
# return updated block

# we will check in descending order of numbers, so take highest indices first
nb_reverse = numberblocks[::-1]

# needed to split the input of the function up into two
# if it was in one, too much for my laptop and it just froze and stopped computing halfway through 
for nb in nb_reverse[:50000]:
    print(nb)
    block = move(nb, block)

for nb in nb_reverse[50000:]:
    print(nb)
    block = move(nb, block)

# calculate final result
result = 0
for num, u in enumerate(block, start = 0):
    if u != ".": result += num * int(u)
    else: pass

print("".join(block))
print("Part 2:", result)