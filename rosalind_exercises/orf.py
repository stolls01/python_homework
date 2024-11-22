from util import reverse_complement
from util import exfasta
from util import transcribe
from util import translate

codons = {
"UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
"UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
"UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
"UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
"UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
"UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
"UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
"UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
"UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
"UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
"UAA": "STOP",     "CAA": "Q",      "AAA": "K",      "GAA": "E",
"UAG": "STOP",    "CAG": "Q",      "AAG": "K",      "GAG": "E",
"UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
"UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
"UGA": "STOP",     "CGA": "R",      "AGA": "R",      "GGA": "G",
"UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G", 
}

filepath = "./rosalind_data/rosalind_orf.txt"
dnadict = exfasta(filepath)

fwrv = []
for value in dnadict.values():
    fwrv.append(value)
    fwrv.append(reverse_complement(value))

transcribed = []
for x in fwrv:
    transcribed.append(transcribe(x))

# for string and reverse string,
    # go along until you find an aug
    # from aug, advance in triplets and translate orf until stop codon or end of string is reached

proteins = []
for s in transcribed:
    current_aug = 0
    for x in range(current_aug, len(s)): # advances along entire string
        triplet = s[x:x+3] # takes three bases with each iteration
        if triplet == "AUG": # searches if the three bases are an aug 
            current_aug = s[x] # so that it skips to next aug on next iteration
            acids = [] # empties temp peptide string for each iteration
            orf = s[x:]
            proteins.append(translate(orf))
            print(translate(orf))


# for some reason, "None" is added once -- remove it
proteins2 = []
for a in proteins:
    if bool(a) is True and a not in proteins2: # to remove duplicates
        proteins2.append(a)

for b in proteins2:
    print(b)