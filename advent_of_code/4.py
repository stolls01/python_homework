from util import read_input
lines = read_input("input_4.txt")

def find_fwrv(lines):
    count = 0
    for line in lines:
        for x in range(len(line)):
            if line[x:x+4] == "XMAS" or line[x:x+4] == "SAMX":
                count += 1
    return count

def lines_vertical(lines):
    vertical = []
    for x in range(len(lines[0])):
        temp = ""
        for line in lines:
            temp += line[x]
        vertical.append(temp)
    return vertical

# x HORIZONTAL
# y VERTICAL
# input is 140x140 matrix

def diagonal(xpos, ypos, lines):
    xlen = len(lines[0])
    ylen = len(lines)
    diag = ""
    if ypos == 0:
        for a in range(xlen - xpos):
            diag += lines[ypos + a][xpos + a]
        return diag
    if xpos == 0:
        for a in range(ylen - ypos):
            diag += lines[ypos + a][xpos + a]
        return diag

linesrv = []
for l in lines:
    linesrv.append(l[::-1])

diagonal_lines = []
for z in range(len(lines)):
    diagonal_lines.append(diagonal(z, 0, lines))
    diagonal_lines.append(diagonal(z, 0, linesrv))
for z in range(1, len(lines)):
    diagonal_lines.append(diagonal(0, z, lines))
    diagonal_lines.append(diagonal(0, z, linesrv))

xmas_count = find_fwrv(lines) + find_fwrv(lines_vertical(lines)) + find_fwrv(diagonal_lines)
print("Part 1:", xmas_count)