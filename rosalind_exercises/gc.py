def gccomp(x):
    gccount = 0
    atcount = 0
    for position in range(len(x)):
        if x[position] == "A" or x[position] == "T":
            atcount = atcount + 1
        else:
            gccount = gccount + 1
    return(gccount / (atcount + gccount))

filepath = "./rosalind_data/rosalind_gc.txt"
with open(filepath, "r") as infile:
    lines = infile.readlines()

# extract descriptions and their index
samples = []
sample_index = []
for line in lines:
    if ">" in line:
        line_stripped = line.strip()
        line_stripped = line_stripped.strip(">")
        samples.append(line_stripped)
        for num, lin in enumerate(lines, 0):
            if line in lin:
                sample_index.append(num)

sample_index.append(len(lines))
y = 0
dnas = []
for x in list(range(len(sample_index) - 1)):
    temp = []
    betw = list(range((sample_index[y] + 1), sample_index[y+1]))
    for ind in betw:
        temp.append(lines[ind].strip())
    tempcat = "".join(temp)
    dnas.append(tempcat)
    y += 1

dnadict = {}
for x in list(range(len(sample_index) -1)):
    dnadict[samples[x]] = dnas[x]

# updates dictionary with gc content
for key in dnadict.keys():
    dnadict[key] = gccomp(dnadict[key])

for key in dnadict.keys():
    if dnadict[key] == max(dnadict.values()):
        print(key.lstrip(">"))
        print(dnadict[key] * 100)