from util import exfasta
from util import transcribe
from util import translate

def splice(rna, introns):
    for t in introns:
        rna = rna.replace(t, "")
    return rna

filepath = "./rosalind_data/rosalind_splc.txt"
dnadict = exfasta(filepath)

rnadict = {}
for keys in dnadict.keys():
    rnadict[keys] = transcribe(dnadict[keys])

unspliced_rna = rnadict[list(rnadict.keys())[0]]
introns = []
for x in range(1, len(rnadict.keys())):
    introns.append(rnadict[list(rnadict.keys())[x]])

spliced_rna = splice(unspliced_rna, introns)
peptide = translate(spliced_rna)
print(peptide)