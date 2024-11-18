#!/usr/bin/env python
#does same as putting in 
#library of utility functions for rosalind exercises

def read_input(filepath):
    with open(filepath, "r") as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

def transcribe(string):
    rna = []
    for nucleotide in string:
        if nucleotide == "T":
            rna.append("U")
        else:
            rna.append(nucleotide)
    rna = "".join(rna)
    return rna

def complement(base):
    if base == "A":
        base = "T"
    elif base == "C":
        base = "G"
    elif base == "G":
        base = "C"
    elif base == "T":
        base = "A"
    return(base)

def reverse_complement(string):
    from util import complement
    c = ""
    for p in range(len(string)):
         c += complement(string[p])
    return(c[::-1])

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

def translate(s, codons):
    acids = []
    for x in range(0, len(s), 3):
        temp = s[x:x+3]
        acid = codons[temp]
        if acid == "STOP":
            return("".join(acids))
        acids.append(acid)
    return("".join(acids))

def hamm(dnas):
    dna1 = dnas[0]
    dna2 = dnas[1]
    hamm = 0
    for position in range(len(dna1)):
        if dna1[position] != dna2[position]:
            hamm += 1
    return hamm