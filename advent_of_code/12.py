from util import read_input
plot = read_input("input_12.txt")


def next_position(grid, positions):
    next_positions = []
    for position in positions:
        next_positions.append(position)
    for position in positions:
        y = int(position[0])
        x = int(position[1])
        value = grid[y][x]
        next_pos = { # if we move, change y, x coordinates depending on which direction
            "left": [0, -1],
            "right": [0, +1],
            "up": [-1, 0],
            "down": [+1, 0],}
        for np in next_pos.values(): # try in every direction: if same letter is there, append that position to our list
            next_x = x + np[1]
            next_y = y + np[0]
            if next_y >= 0 and next_y < len(grid) and next_x >= 0 and next_x < len(grid[0]):        # if it isnt out of bounds    
                next_position = grid[next_y][next_x]
                if [next_y, next_x] not in next_positions and next_position == value:
                    next_positions.append([next_y, next_x])
    return next_positions # get the locations of all same leters -- can feed those into function again to work our way up to 9

def get_entire_region(grid, positions):
    regions = {}
    for num, position in enumerate(positions):
        status = True
        for r in regions.values():
            if position in r:
                status = False
        if status is True:
            position = [position] # put all into extra list to make it workable for the function, it expects list(s) in a list
            while position != next_position(grid, position):
                position = next_position(grid, position)            
            regions[num] = position
    return regions

def is_adjacent(pos1, pos2):
    if (pos1[0] == pos2[0] and abs(pos1[1]-pos2[1]) == 1) or\
        (pos1[1] == pos2[1] and abs(pos1[0]-pos2[0]) == 1): # if difference between positions is [1, 0] or [0, 1]
        return True

def main():
    all_positions = []
    for y in range(len(plot)):
        for x in range(len(plot[1])):
            all_positions.append([y, x])

    plots = get_entire_region(plot, all_positions)
    print(plots)
    edge_counts = {}
    for key, value in plots.items():
        edge_counts[key] = 0
        edge_count = 0
        for p1 in plots[key]:
            edges = 4
            for p2 in plots[key]:
                if p1 == p2:
                    continue
                else:
                    if is_adjacent(p1, p2):
                        edges += -1
            edge_count += edges
        edge_counts[key] = edge_count


    total_price = 0
    for letter in plots.keys():
        price = len(plots[letter]) * edge_counts[letter]
        total_price += price

    print("Part 1:", total_price)

if __name__ == "__main__":
    main()