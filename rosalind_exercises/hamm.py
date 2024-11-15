
filepath = "./rosalind_data/rosalind_hamm.txt"
with open(filepath, "r") as infile:
    lines = infile.readlines()
    dna1 = lines[0].rstrip()
    dna2 = lines[1].rstrip()

hamm = 0

for position in range(len(dna1)):
    if dna1[position] != dna2[position]:
        hamm = hamm + 1
    
print(hamm)