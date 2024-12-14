from util import read_input
import time
import copy
raw = read_input("input_14.txt")

def move(grid, values):
    for value in values:
        position = value[0]
        velocity = value[1]
        x = position[0]
        y = position[1]

        # remove previous marking on tiles
        grid[y][x] -= 1 

        # calculate new position based on velocity
        new_x = position[0] + velocity[0]
        new_y = position[1] + velocity[1]

        # if new position is out of range, continue counting into other side
        while new_x > len(grid[0])-1: new_x = new_x - len(grid[0])
        while new_x < -(len(grid[0])-1): new_x = new_x - -(len(grid[0]))
        while new_y > len(grid)-1: new_y = new_y - len(grid)
        while new_y < -(len(grid)-1): new_y = new_y - -(len(grid))

        # update grid
        grid[new_y][new_x] += 1
        
        # update the position in our index list for next iteration
        value[0] = [new_x, new_y]

def quadrant_sum(tiles, a, x_len, b, y_len):
    sum = 0
    for x in range(a, x_len):
        for y in range(b, y_len):
            sum += tiles[y][x]
    return sum

def main():
    # transform input data into something useable
    pos_vel = {}
    for num, line in enumerate(raw):
        pos_vel[num] = []
        p = line.split(" ")[0]
        v = line.split(" ")[1]
        p = p.split("=")[1]
        v = v.split("=")[1]
        position = []
        position.append(int(p.split(",")[0]))
        position.append(int(p.split(",")[1]))
        pos_vel[num].append(position)
        velocity = []
        velocity.append(int(v.split(",")[0]))
        velocity.append(int(v.split(",")[1]))
        pos_vel[num].append(velocity)

    tiles = [[0 for col in range(101)] for row in range(103)]

    # establish first position in starting matrix
    for key, value in pos_vel.items():
        position = value[0]
        velocity = value[1]
        x = int(position[0])
        y = int(position[1])
        tiles[y][x] += 1

    # copy to reuse for part two
    tiles2 = copy.deepcopy(tiles)
    pos_vel2 = copy.deepcopy(pos_vel)

    # # calculate the result
    x_len = len(tiles[0])
    y_len = len(tiles)

    if x_len % 2 == 0: half_x = x_len / 2
    else: half_x = int((x_len-1) / 2)

    if y_len % 2 == 0: half_y = y_len / 2
    else: half_y = int((y_len-1) / 2)


    # PART ONE
    for h in range(100):
        move(tiles, pos_vel.values())

    final_product = 1
    final_product *= quadrant_sum(tiles, 0, half_x, 0, half_y)
    final_product *= quadrant_sum(tiles, half_x + 1, x_len, 0, half_y)
    final_product *= quadrant_sum(tiles, 0, half_x, half_y + 1, y_len)
    final_product *= quadrant_sum(tiles, half_x + 1, x_len, half_y + 1, y_len)

    print("Part 1:", "danger sum", final_product)

    # PART TWO
    # danger sum will be low if lots of positions are together in same quadrant = form tree
    danger_sum = 500000000
    for h in range(10000):
        move(tiles2, pos_vel2.values())

        final_product = 1
        final_product *= quadrant_sum(tiles2, 0, half_x, 0, half_y)
        final_product *= quadrant_sum(tiles2, half_x + 1, x_len, 0, half_y)
        final_product *= quadrant_sum(tiles2, 0, half_x, half_y + 1, y_len)
        final_product *= quadrant_sum(tiles2, half_x + 1, x_len, half_y + 1, y_len)

        if final_product < danger_sum:
            danger_sum = final_product
            iteration = h

    print("Part 2:", "danger sum", danger_sum, ", iteration", iteration + 1)

if __name__ == "__main__":
    main()