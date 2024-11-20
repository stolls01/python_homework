####### conceptually:
# 1. need key-value pairs of codons and corresponding acid
# 2. read a string in pieces of three
# 3. translate each triple into an amino acid
# 4. add each amino acid to final string
# 5. stop it at "STOP"
# 6. print it

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

def translate(s):
    acids = ""
    for x in range(0, len(s), 3): # advances along entire string in steps of 3
        triple = s[x:x+3] # takes three bases with each iteration
        acid = codons[triple]
        if acid == "STOP":
            return(acids) # returns sequence when stop codon is reached
        acids += acid


string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"    
print(translate(string))