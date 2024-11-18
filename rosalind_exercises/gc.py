from util import read_input

def gccomp(x):
    gccount = 0
    atcount = 0
    for position in range(len(x)):
        if x[position] == "G" or x[position] == "C":
            gccount += 1
    return((gccount / len(x)) * 100)

filepath = "./rosalind_data/rosalind_gc.txt"

#returns a dictionary with respective dna identifiers and dna strings
#def exfasta(filepath):
infile = read_input(filepath)
samples = []
dnas = []
temp = ""
for line in infile:
    if ">" in line:
        samples.append(line) # adds dna indices to samples list
        if bool(temp) is True:
            dnas.append(temp) # each time a new dna index is reached, it compiles the in temp saved string of previous dna (if present) and adds it to list
        temp = ""
    elif ">" not in line and line == infile[(len(infile)-1)]: #if it is final line of document
        dnas.append(temp)
    elif ">" not in line:
        temp += line

dnadict = {}
for x in range(len(dnas)):
    dnadict[samples[x].lstrip(">")] = dnas[x]

# updates dictionary with gc content
for key in dnadict.keys():
    dnadict[key] = gccomp(dnadict[key])

for key in dnadict.keys():
    if dnadict[key] == max(dnadict.values()):
        print(key.lstrip(">"))
        print(dnadict[key])



