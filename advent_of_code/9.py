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


# get the indeces of file blocks
numberblocks = []
for num, x in enumerate(block_flipped, start = 0):
    status = False
    if x == ".":
        continue
    if x != ".":
        for y in range(10):
            if num+y < len(block_flipped)-1 and block_flipped[num + y] != x and status is False:
                filestart = num
                fileend = num + y
                if fileend not in [b[1] for b in numberblocks]:
                    numberblocks.append([filestart, fileend])
                status = True

print(numberblocks)

#################
# walk along original block -- if encountering a . : calculate distance  to next non-dot
# go through all numberblocks: if they cover less distance than dot-distance: replace dots with that numberblock
block_two = copy.deepcopy(orig_block)

status = False
for i, b in enumerate(numberblocks):
    block_length = b[1]-b[0]
    for num, x in enumerate(block_two, start = 0):
        if x == ".":
            for y in range(9):
                if num+y < len(block_two)-1 and block_two[num + y] != '.' and status is False:
                    status = True
                    dotstart = num
                    dotend = num + y
                    dot_length = y
                    status = True
            if b[1]-b[0] <= dot_length:
                block_two[dotstart:(dotstart+b[1]-b[0])] = block_flipped[b[0]:b[1]]


            # # print(block_two[dotstart:(dotstart+b[1]-b[0])])
            # if b[1]-b[0] > dot_length:
            #     continue
            # if b[1]-b[0] <= dot_length:
            #     block_two[dotstart:(dotstart+b[1]-b[0])] = block_flipped[b[0]:b[1]]
            #     # remove numberblock from blocks list
            #     for j in b:
            #         for k in range(dotend, len(block_two)):
            #             if block_two[k] == block_flipped[j]:
            #                 block_two[k] = "."
            #     status = True
            #     break
print("numberblocks", numberblocks)

print("UPDATED", block_two)
print("".join(block_two))
# print("".join(block_two))
# print("".join(block_flipped))
# for f in block_flipped:


#     if f != ".":
#         for num, o in enumerate(updated_block, start = 0):
#             if o == ".":
#                 print("num", num)
#                 updated_block[num] = f
#                 break
#     if f == ".":
#         updated_block = updated_block[:-1]

# result = 0
# for num, u in enumerate(updated_block, start = 0):
#     result += num * int(u)

# print(result)






# for d in dots:
#     print(orig_block[d[0]:d[1]])

# for d in blocks:
#     print(block_flipped[d[0]:d[1]])






# PART ONE
# updated_block = orig_block
# for f in block_flipped:
#     if f != ".":
#         for num, o in enumerate(updated_block, start = 0):
#             if o == ".":
#                 print("num", num)
#                 updated_block[num] = f
#                 break
#     if f == ".":
#         updated_block = updated_block[:-1]

# result = 0
# for num, u in enumerate(updated_block, start = 0):
#     result += num * int(u)

# print(result)