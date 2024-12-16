from util import read_input
import copy
import time
import os
raw = read_input("input_15.txt")

map = []
movements = ""
for r in raw:
    if "#" in r:
        map.append(r)
    else:
        movements += r

for m in map:
    print(m)
print(movements)

# get original position of robot
for num, line in enumerate(map):
    if "@" in line:
        for i in range(len(line)):
            if line[i] == "@":
                orig_position = [num, i]

next_index = {
        "^": [-1, 0],
        ">": [0, +1],
        "v": [+1, 0],
        "<": [0, -1]}

def move_box(map, next_index, direction, position):
    if len(map) > len(map[0]): map_len = len(map) 
    else: map_len = len(map[0])
    orig_position = position
    
    y = position[0]
    x = position[1]
    next_y = next_index[direction][0]
    next_x = next_index[direction][1]

    position = [y + next_y, x + next_x]

    # z is distance between @, x amount of Os, and .
    for z in range(0, map_len):
        if map[y + z*next_y][x + z*next_x] == "#":
            return [map, orig_position]
        if map[y + z*next_y][x + z*next_x] == "O":
            pass
        if map[y + z*next_y][x + z*next_x] == ".":
            distance = z
            break
    
    if direction == ">":
        line = copy.deepcopy(map[y])
        map[y] = line[:x] + "." + line[x:x+(z*next_x)] + line[x+(z*next_x)+1:]
        return [map, position]

    if direction == "<":
        line = copy.deepcopy(map[y])
        map[y] = line[:x + (z*next_x)] + line[x+(z*next_x)+1:x+1] + "." + line[x+1:]
        return [map, position]

    if direction == "^" or direction == "v":
        x_line = ""
        for m in range(len(map)):
            x_line += map[m][x]

        line = copy.deepcopy(x_line)

        if direction == "^":
            x_line = line[:y + (z*next_y)] + line[y+(z*next_y)+1:y+1] + "." + line[y+1:]
        if direction == "v":
            x_line = line[:y] + "." + line[y:y+(z*next_y)] + line[y+(z*next_y)+1:]

        for i in range(len(x_line)):
            map[i] = map[i][:x] + x_line[i] + map[i][x+1:]
        return [map, position]


position = orig_position
for direction in movements: # until all of them are done
    y = position[0]
    x = position[1]
    next_y = next_index[direction][0]
    next_x = next_index[direction][1]
    os.system('cls')
    for m in map:
        print(m)
    # check whether next position according direction is #, do nothing
    if map[y + next_y][x + next_x] == "#": # works
        continue

    # move along if theres nothing there
    if map[y + next_y][x + next_x] == ".": # works
        position = [y + next_y, x + next_x]
        line = copy.deepcopy(map[y])
        map[y] = line[:x] + "." + line[x+1:]
        map[y + next_y] = map[y + next_y][:x + next_x] + "@" + map[y + next_y][x + next_x +1:]
        continue

    # otherwise move the whole block up by one
    if map[y + next_y][x + next_x] == "O":
        map = move_box(map, next_index, direction, position)[0]
        position = move_box(map, next_index, direction, position)[1]
        continue


for m in map:
    print(m)

gps = 0

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "O":
            gps += 100 * y + x

print("Part 1:", gps)