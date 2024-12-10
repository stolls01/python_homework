from util import read_input
lines = read_input("input_10.txt")

#0123
#1234
#8765
#9876

# get positions of 0s
starts = []
for x in range(len(lines[0])):
    for y in range(len(lines)):
        if lines[y][x] == "0":
            starts.append([y, x])

# get positions of 9s
ends = []
for x in range(len(lines[0])):
    for y in range(len(lines)):
        if lines[y][x] == "9":
            ends.append([y, x])

def next_position(grid, positions):
    next_positions = []
    for position in positions:
        y = int(position[0])
        x = int(position[1])
        value = int(grid[y][x])
        next_pos = { # if we move, change y, x coordinates depending on which direction
            "left": [0, -1],
            "right": [0, +1],
            "up": [-1, 0],
            "down": [+1, 0],}
        for np in next_pos.values(): # try in every direction: if our value + 1 is there, append that position to our list
            next_x = x + np[1]
            next_y = y + np[0]
            if (next_y >= 0 and next_y < len(grid)) and (next_x >= 0 and next_x < len(grid[0])):        # if it isnt out of bounds    
                next_position = int(grid[next_y][next_x])
                if int(next_position) == int(value) + 1:
                    next_positions.append([next_y, next_x])
    return next_positions # get the locations of all number + 1s -- can feed those into function again to work our way up to 9


######### PART ONE
def final_position(grid, positions):
    count = 0
    for position in positions:
        position = [position] # put all into extra list to make it workable for the function, it expects list(s) in a list
        for t in range(9): # with each iteration, we move one digit up until we ideally arrive at 9
            position = next_position(grid, position)
        for nineindex in ends: # for all the 9s which are in original grid -- if we arrived at their locations via our paths, add to score
            if nineindex in position:
                count += 1
    return count

print("Part 1:", final_position(lines, starts))


######### PART TWO
# need to find ALL possible paths which arrive at a 9
def final_position(grid, positions):
    count = 0
    for position in positions:
        position = [position]
        for t in range(9): # with each iteration, we move one digit up until we ideally arrive at 9
            position = next_position(grid, position) # function returns all possible paths, but this time we dont look for unique 9s
        count += len(position)  # each time we arrived at a 9, we saved its index
                                #-- just need to count how often we did = how many times an index was saved
    return count

print("Part 2:", final_position(lines, starts))
