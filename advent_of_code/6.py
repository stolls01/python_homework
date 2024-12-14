from util import read_input
lines = read_input("input_6.txt")
import time
import os
import copy

turn = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"}

next_index = {
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

def count_turns(lines, start_position, n_turns):
    position = start_position
    visited_positions = []
    direction = "^"
    
    for i in range(n_turns):
        y = position[0]
        x = position[1]

        # # printing !!
        lines[y] = lines[y][:x] + direction + lines[y][x+1:]
        os.system("cls")
        for line in lines[:y+30]: # cut off lower part where nothing happens, otherwise it flickers even more
            print(line)
        # # time.sleep(0.05) # would take forever with big input                    

        # if out of bounds, it breaks
        if y <= 0 or x >= len(lines[0]) or y+1 == (len(lines)) or x <= 0:
            break

        # check whether next position according direction is # or not, advance accordingly
        for arrow in turn.keys(): # directions
            if direction == arrow:
                next_y = next_index[arrow][0]
                next_x = next_index[arrow][1]
                if lines[y+next_y][x+next_x] != "#":
                    position = [y + next_y, x + next_x]
                    visited_positions.append(position)
                if lines[y + next_y][x + next_x] == "#":
                    direction = turn[direction]
        #print("Visited Positions", visited_positions)
    return visited_positions

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
                next_y = y + next_index[arrow][0]
                next_x = x + next_index[arrow][1]

                # if next position is not a #, move there
                if lines[next_y][next_x] != "#":
                    position = [next_y, next_x]

                # if encountering #, turn and save that position for later reference
                if lines[next_y][next_x] == "#": # to avoid error with indices at edges
                    if (str(y) + "," + str(x) + "," + direction) in visited_turns:
                        return True
                    visited_turns.append(str(y) + "," + str(x) + "," + direction)
                    direction = turn[direction]


################# PART ONE
def unique_count(lines, i):
    unique_positions = []
    for v in count_turns(lines, orig_position, i):
        if v not in unique_positions:
            unique_positions.append(v)
    return [unique_positions, len(unique_positions)]

print("Part 1:", unique_count(lines, 6000)[1])

################## PART TWO

unique_positions = unique_count(lines, 6000)[0]
loop_count = 0

# for all positions that the cursor runs along in original scenario:
# place a block there, run scenario -- if it returns a loop (True), add to count

for u in unique_positions:
    y = u[0]
    x = u[1]
    if (y == orig_position[0] and x == orig_position[1]): # throws error if you replace the arrow
        pass
    else:
        newline = lines[y][:x] + "#" + lines[y][x+1:] #  place a block
        lines2 = copy.deepcopy(lines)
        lines2[y] = newline
        if find_loops(lines2, orig_position, 10000) is True:
            loop_count += 1

print("Part 2:", loop_count)