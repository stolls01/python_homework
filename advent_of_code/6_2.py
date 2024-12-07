from util import read_input
import copy
lines = read_input("input_6.txt")

turn = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"}

next_pos = {
        "^": [-1, 0],
        ">": [0, +1],
        "v": [+1, 0],
        "<": [0, -1]}

# get original position
for num, line in enumerate(lines):
    if "^" in line:
        for i in range(len(line)):
            if line[i] == "^":
                orig_position = [num, i]

def find_loops(lines, start_position, n_turns):
    position = start_position
    visited_turns = []
    direction = "^"

    for i in range(n_turns):
        y = position[0]
        x = position[1]

        # if next position would be out of bounds, move on to next permutation
        if y <= 0 or x >= len(lines[0])-1 or y >= (len(lines))-1 or x <= 0:
            break

# at each turn of a #, the respective coordinates + direction are added to visited turns list
# at each turn, we check: if it is already in list, we were here before -- its a loop!

        for arrow in turn.keys(): # directions
            if direction == arrow:
                # depending which direction we're facing, retrieval of the next position
                next_y = y + next_pos[arrow][0]
                next_x = x + next_pos[arrow][1]

                # if next position is not a #, move there
                if lines[next_y][next_x] != "#":
                    position = [next_y, next_x]

                # if encountering #, turn and save that position for later reference
                if lines[next_y][next_x] == "#": # to avoid error with indices at edges
                    if (str(y) + "," + str(x) + "," + direction) in visited_turns:
                        return True
                    visited_turns.append(str(y) + "," + str(x) + "," + direction)
                    direction = turn[direction]

# find all permutations of matrix, each time one index replaced by #
# run it through function -- if it returns a loop (True), add to count
loop_count = 0
iteration = 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (y == orig_position[0] and x == orig_position[1]):
            pass
        else:
            print(iteration)
            iteration += 1
            newline = lines[y][:x] + "#" + lines[y][x+1:]
            lines2 = copy.deepcopy(lines)
            lines2[y] = newline
            if find_loops(lines2, orig_position, 10000) is True:
                loop_count += 1

print("Part 2:", loop_count)