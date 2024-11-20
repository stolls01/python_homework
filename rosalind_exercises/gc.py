from util import read_input

def gccomp(x):
    gccount = 0
    for position in range(len(x)):
        if x[position] == "G" or x[position] == "C":
            gccount += 1
    return((gccount / len(x)) * 100)

# alternatively how to count
# dna = "GATTACCA"
# for base in dna:
#     counts[base] += 1

# OR built-in:
# dna.count("C")



#returns a dictionary with respective dna identifiers and dna strings
#def exfasta(filepath):
def exfasta(filepath):
    infile = read_input(filepath)
    samples = []
    dnas = []
    temp = ""
    for line in infile:
        if line[0] == ">":
            samples.append(line) # adds dna indices to samples list
            if bool(temp) is True: # so that establishing temp = "" string doesnt occupy dnas[0]
                dnas.append(temp) # each time a new dna index is reached, it compiles the in temp saved string of previous dna (if present) and adds it to list
            temp = ""
        elif ">" not in line and line == infile[(len(infile)-1)]: #if it is final line of document
            temp += line
            dnas.append(temp)
        elif ">" not in line:
            temp += line
    dnadict = {}
    for x in range(len(dnas)):
        dnadict[samples[x].lstrip(">")] = dnas[x]
    return dnadict

filepath = "./rosalind_data/rosalind_gc.txt"
dnadict = exfasta(filepath)

# updates dictionary with gc content
for key in dnadict.keys():
    dnadict[key] = gccomp(dnadict[key])

for key in dnadict.keys():
    if dnadict[key] == max(dnadict.values()):
        print(key)
        print(dnadict[key])



