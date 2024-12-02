from util import exfasta

filepath = "./rosalind_data/rosalind_cons.txt"
dnas = list(exfasta(filepath).values())
profilematrix = {}

for i in range(len(dnas[0])):
    counter = {"A": 0, "C": 0, "G": 0, "T": 0}
    for dna in dnas:
        for key in counter.keys():
            if dna[i] == key:
                counter[key] += 1
    for acgt in "ACGT":
        if i == 0:
            profilematrix[acgt] = [] # establishes that the dictionary has lists as values
        profilematrix[acgt].append(counter[acgt])

#print(profilematrix)
#{'A': [5, 1, 0, 0, 5, 5, 0, 0], 'C': [0, 0, 1, 4, 2, 0, 6, 1], 'G': [1, 1, 6, 3, 0, 1, 0, 0], 'T': [1, 5, 0, 0, 0, 1, 1, 6]}

consensus = ""
for p in range(len(dnas[0])):
    max_frequency = 0
    most_frequent_base = ""
    for key, value in profilematrix.items():
        if value[p] > max_frequency:
            max_frequency = value[p]
            most_frequent_base = key
    consensus += most_frequent_base

print(consensus)
for key, value in profilematrix.items():
    print(key + ": " + ' '.join(str(x) for x in value))