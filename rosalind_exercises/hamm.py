
from util import read_input

filepath = "./rosalind_data/rosalind_hamm.txt"
dnas = read_input(filepath)
dna1 = dnas[0] # line 1
dna2 = dnas[1] # line 2

def hamm(dna1, dna2):
    hamm = 0
    for position in range(len(dna1)):
        if dna1[position] != dna2[position]:
            hamm += 1
    return hamm

print(hamm(dna1, dna2))