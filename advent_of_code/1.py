from input_1 import input
# manually edited input to make it into dictionary

left_list = []
right_list = []

for key, value in input.items():
    left_list.append(key)
    right_list.append(value)

left_list.sort()
right_list.sort()

common = {}
for i in range(len(left_list)):
    common[left_list[i]] = right_list[i]

difference = []                                 # PART ONE
for key, value in common.items():
    diff = key - value
    difference.append(abs(diff))
final = 0
for d in difference:
    final += d
print("Part 1:", final)


similarity_score = 0                            # PART TWO
for l1 in common.keys():
    freq = 0
    for l2 in common.values():
        if l1 == l2: freq += 1
    similarity_score += l1 * freq
print("Part 2:", similarity_score)