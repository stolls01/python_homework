from util import reverse_complement
from util import exfasta
from util import transcribe
from util import translate

filepath = "./rosalind_data/rosalind_orf.txt"
dna = list(exfasta(filepath).values())[0]

fwrv = []
fwrv.append(dna)
fwrv.append(reverse_complement(dna))

transcribed = []
for x in fwrv:
    transcribed.append(transcribe(x))

# for string and reverse string,
    # go along until you find an aug
    # from aug, advance in triplets and translate orf until stop codon or end of string is reached

proteins = []
for s in transcribed: # for string and reverse string
    for x in range(len(s)): 
        triplet = s[x:x+3] # go along entire string in triplets until you find an aug
        if triplet == "AUG":
            orf = s[x:] # use previously established translate function on current reading frame
            # translate function is set up such that it will return a peptide string if a stop codon is in orf, else "None"
            if bool(translate(orf)) is True and translate(orf) not in proteins: # prevents duplicates and failed translations
                proteins.append(translate(orf))
                print(translate(orf))