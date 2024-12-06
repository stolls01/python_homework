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
position_hat = position

def find_loops(lines, n_turns):
    position = position_hat
    visited_positions = []
    visited_turns = []
    direction = "^"

    for i in range(n_turns):
        
        # for easier reading of coordinates
        y = position[0]
        x = position[1]

        # if out of bounds it breaks
        if y-1 < 0 or x+1 > len(lines[9])-1 or y+1 > (len(lines)-1) or x-1 < 0:
            break

# at each turn of a #, the respective coordinates + direction are added to visited turns list
# at each turn, it's checked against that list. if it already exists -- its a loop!
# just trust that it works, id rather kms than try to decipher this mess of a code again
        for hat in turns.keys(): # directions
            if direction == hat:
                indeces = next_pos[hat]
                # in line
                if lines[y + (indeces[0])][x + (indeces[1])] != "#":
                    position = [y+(indeces[0]), x+(indeces[1])]
                if (str(y) + str(x) + direction) in visited_turns:
                    return True
                visited_turns.append(str(y) + str(x) + direction)
                # turns
                if lines[y + (indeces[0])][x + (indeces[1])] == "#":
                    direction = turns[direction]
                
        #print("Visited Positions", visited_positions)
    
# find all permutations of matrix, each time one index replaced by #
# run it through adjusted function -- if it returns a loop, add it to count
loop_count = 0
permutation = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        permutation += 1
        print(permutation)
        if y == position_hat[0] and x == position_hat[1]:
            break
        newline = lines[y][:x] + "#" + lines[y][x+1:]
        lines2 = lines.copy()
        lines2.pop(y)
        lines2.insert(y, newline)
        if find_loops(lines2, 5500) is True:
            loop_count += 1

print("Part 2:", loop_count)