from util import read_input
import copy

lines = read_input("input_8.txt")

# get unique antennas
antennas = []
for line in lines:
    for x in range(len(line)):
        if line[x] not in antennas:
            antennas.append(line[x])

# per antennas, get all occurrences in grid
frequencies = {}
for a in antennas:
    if a != ".":
        frequencies[a] = []
        for num, line in enumerate(lines):
            if a in line:
                for i in range(len(line)):
                    if line[i] == a:
                        frequencies[a].append([num, i])

# find antinodes of two antennas of the same frequency
def antinode(a, b):
# antinode([5, 6], [8, 8])
    nodes = []
    y_diff = a[0] - b[0]
    x_diff = a[1] - b[1]
    nodes.append([a[0] - 2*y_diff, a[1] - 2*x_diff])
    nodes.append([b[0] + 2*y_diff, b[1] + 2*x_diff])
    return nodes

# get all combinations within one frequency, for all frequencies
def get_all_antinodes(frequencies):
    all_antinodes = []
    for symbol, positions in frequencies.items():
        for first_coordinate in range(len(positions)):
            a = positions[first_coordinate]
            for second_coordinate in range(len(positions)):
                b = positions[second_coordinate]
                if a != b:
                    all_antinodes.append(antinode(a, b))
    return all_antinodes

all_antinodes = get_all_antinodes(frequencies)

print("antinodes", all_antinodes)


def count_nodes(all_antinodes):
    updated_lines = copy.deepcopy(lines)
    count = 0
    for f in all_antinodes:
        for g in f:
            a = g[0]
            b = g[1]
            if a < len(updated_lines) and a >= 0 and b < len(updated_lines[0]) and b >= 0:
                if updated_lines[a][b] != "#": # we are looking for unique antinodes
                    newline = updated_lines[a][:b] + "#" + updated_lines[a][b+1:]
                    updated_lines[a] = newline
                    count += 1
                else:
                    pass
    for u in updated_lines:
        print(u)
    return count

print("Part 1:", count_nodes(all_antinodes))

############################# PART TWO
# nodes need to be created not just in twice the distance, but along the entire line
# replace *2 multiplication with every z in length(grid) to antinode function

print("\n-----------------------------------------\n")

def antinode(a, b):
    nodes = []
    y_diff = a[0] - b[0]
    x_diff = a[1] - b[1]
    for z in range(len(lines)): 
        nodes.append([a[0] - z * y_diff, a[1] - z * x_diff])
        nodes.append([b[0] + z * y_diff, b[1] + z * x_diff])
    return nodes

all_antinodes = get_all_antinodes(frequencies)
print("Part 2:", count_nodes(all_antinodes))