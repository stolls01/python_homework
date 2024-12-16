from util import read_input
import copy
import time
import os

raw = read_input("input_15.txt")

def widen(map):
    map2 = []
    for i in range(len(map)):
        map2.insert(i, "")
        for j in map[i]:
            if j == "#": map2[i] += j + j
            if j == ".": map2[i] += j + j
            if j == "@": map2[i] += "@."
            if j == "O": map2[i] += "[]"
    return map2

def box_positions(position, boxes, map, z):
    positions = []
    for b in boxes:
        y = b[0]
        x = b[1]

        if b == position:
            if map[y + z][x] == "#": return False
            elif map[y + z][x] == "[": positions.append([y+z, x])
            elif map[y + z][x] == "]": positions.append([y+z, x-1])

        # check if there is a box in front of the box
        if b != position:
            if map[y + z][x] == "#": return False
            if map[y + z][x + 1] == "#": return False
            if map[y + z][x] == "[": positions.append([y+z, x])
            if map[y + z][x] == "]": positions.append([y+z, x-1])
            if map[y + z][x + 1] == "[": positions.append([y+z, x + 1])
        
    for p in positions:
        if p not in boxes: boxes.append(p)
    return boxes


def move_box(map, next_index, direction, position):

    y = position[0]
    x = position[1]
    next_y = next_index[direction][0]
    next_x = next_index[direction][1]

    if direction == ">" or direction == "<":

        # q is distance between @, x amount of Os, and .
        for q in range(0, 20):
            if map[y + q*next_y][x + q*next_x] == "#": return [map, position]
            if map[y + q*next_y][x + q*next_x] == "[": pass
            if map[y + q*next_y][x + q*next_x] == "]": pass
            if map[y + q*next_y][x + q*next_x] == ".":
                distance = q
                break

        line = copy.deepcopy(map[y])

        if direction == ">":
            position = [y + next_y, x + next_x]
            map[y] = line[:x] + "." + line[x:x+distance] + line[x+distance+1:]
            return [map, position]

        if direction == "<":
            position = [y + next_y, x + next_x]
            map[y] = line[:x - distance] + line[x-distance+1:x+1] + "." + line[x+1:]
            return [map, position]


    if direction == "v" or direction == "^":
        if direction == "v": z = 1
        elif direction == "^": z = -1
        
        positions = [position] # put into extra lists because function takes lists inside lists, e.g. [[1, 2]]
        for i in range(20):
            positions = box_positions(position, positions, map, z)
            if positions is False:
                status = False
                box_cluster = []
                break
            positions == box_positions(position, positions, map, z)
            box_cluster = positions
            status = True
        
        if status is True:
            map2 = copy.deepcopy(map)

            for c in box_cluster: # remove the old markings with dots
                yy = c[0]
                xx = c[1]
                if map2[yy][xx] == "@":
                    map[yy] = map2[yy][:xx] + "." + map[yy][xx+1:]
                elif map2[yy][xx] == "[":
                    map[yy] = map[yy][:xx] + ".." + map[yy][xx+2:]

            for c in box_cluster: # add new markings of boxes
                yy = c[0]
                xx = c[1]
                if map2[yy][xx] == "[":
                    map[yy+z] = map[yy+z][:xx] + "[]" + map[yy+z][xx+2:]
                elif map2[yy][xx] == "@":
                    map[yy+z] = map[yy+z][:xx] + "@" + map[yy+z][xx+1:]

            position = [y + next_y, x + next_x]

    return [map, position]


def main():
    # differentiate in input between map setup and movements
    map = []
    movements = ""
    for r in raw:
        if "#" in r: map.append(r)
        else: movements += r

    # for part two, make 0 into []
    map = widen(map)

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
    
    position = orig_position
    for direction in movements: # until all of them are done
        y = position[0]
        x = position[1]
        next_y = next_index[direction][0]
        next_x = next_index[direction][1]

        # time.sleep(0.05)
        # os.system('cls')
        # for m in map:
        #     print(m)

        # check whether next position according direction is #, do nothing
        if map[y + next_y][x + next_x] == "#":
            continue

        # move along if theres no block or box
        if map[y + next_y][x + next_x] == ".":
            position = [y + next_y, x + next_x]
            line = copy.deepcopy(map[y])
            map[y] = line[:x] + "." + line[x+1:]
            map[y + next_y] = map[y + next_y][:x + next_x] + "@" + map[y + next_y][x + next_x +1:]
            continue

        # otherwise move the whole block of boxes up by one
        if map[y + next_y][x + next_x] == "[":
            map = move_box(map, next_index, direction, position)[0]
            position = move_box(map, next_index, direction, position)[1]
            continue

        if map[y + next_y][x + next_x] == "]":
            map = move_box(map, next_index, direction, position)[0]
            position = move_box(map, next_index, direction, position)[1]
            continue

    gps = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "[":
                gps += 100 * y + x

    for m in map:
        print(m)
    print("Part 2:", gps)

if __name__ == "__main__":
    main()