from util import read_input
lines = read_input("input_6.txt")
# lines = [
#  '....#.....',
#  '.........#',
#  '..........',
#  '..#.......',
#  '.......#..',
#  '..........',
#  '.#..^.....',
#  '........#.',
#  '#.........',
#  '......#...']

turns = {
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
                position = [num, i]

def count_turns(lines, n_turns):
    visited_positions = []
    direction = "^"
    
    for i in range(n_turns):
        y = position[0]
        x = position[1]

        # if out of bounds it breaks
        if (direction == "^" and y-1 < 0) or\
        (direction == ">" and x+1 > len(lines[9])-1) or\
        (direction == "v" and y+1 > len(lines)-1) or\
        (direction == "<" and x-1 < 0):
            break

        for hat in turns.keys(): # directions
            if direction == hat:
                indeces = next_pos[hat]
                if lines[y+(indeces[0])][x+(indeces[1])] != "#":
                    position = [y+(indeces[0]), x+(indeces[1])]
                    visited_positions.append(position)
                if lines[y+(indeces[0])][x+(indeces[1])] == "#":
                    direction = turns[direction]
        #print("Visited Positions", visited_positions)
    return visited_positions

# PART ONE
def unique_count(lines, i):
    unique_positions = []
    for v in count_turns(lines, i):
        if v not in unique_positions:
            unique_positions.append(v)
    return len(unique_positions)

print("Part 1:", unique_count(lines, 5500))