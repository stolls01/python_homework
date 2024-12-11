from util import read_input
lines = read_input("input_6.txt")
import time
import os

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

def count_steps(lines, start_position, n_turns):
    position = start_position
    visited_positions = []
    direction = "^"
    
    for i in range(n_turns):
        y = position[0]
        x = position[1]
        # if out of bounds, it breaks
        if y <= 0 or x >= len(lines[0])-1 or y >= (len(lines))-1 or x <= 0:
            break

        for arrow in turn.keys(): # directions
            if direction == arrow:
                next_y = next_index[arrow][0]
                next_x = next_index[arrow][1]
                if lines[y+next_y][x+next_x] != "#":
                    position = [y + next_y, x + next_x]
                    y = position[0]
                    x = position[1]
                    visited_positions.append(position)
                    lines[y] = lines[y][:x] + direction + lines[y][x+1:]
                    os.system("cls")
                    for line in lines:
                        print(line)
                    # time.sleep(0.1) # would take forever with big input
                if lines[y + next_y][x + next_x] == "#":
                    direction = turn[direction]
        #print("Visited Positions", visited_positions)
    return visited_positions

# PART ONE
def unique_count(lines, i):
    unique_positions = []
    for v in count_steps(lines, orig_position, i):
        if v not in unique_positions:
            unique_positions.append(v)
    return len(unique_positions)

print("Part 1:", unique_count(lines, 6000))