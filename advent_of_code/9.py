from util import read_input
import copy
lines = read_input("input_9.txt")
input = ""
for line in lines:
    input += line

#test
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

print(orig_block)
block_flipped = orig_block[::-1]
#print("".join(orig_block))
## 00...111...2...333.44.5555.6666.777.888899
#print("".join(block_flipped))
# 998888.777.6666.5555.44.333...2...111...00

updated_block = orig_block
for f in block_flipped:
    if f != ".":
        for num, o in enumerate(updated_block, start = 0):
            if o == ".":
                print("num", num)
                updated_block[num] = f
                break
    if f == ".":
        updated_block = updated_block[:-1]

result = 0
for num, u in enumerate(updated_block, start = 0):
    result += num * int(u)

print("".join(updated_block))
print(result)