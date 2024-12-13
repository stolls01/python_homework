from util import exfasta

filepath = "test.txt"
dnadict = exfasta(filepath)

def main():
    adjacencies = []
    k = 3
    for identifier, dna in dnadict.items():
        for id, dna_2 in dnadict.items():
            if dna == dna_2:
                continue
            if dna[len(dna)-k:] == dna_2[:k]:
                adjacencies.append([identifier, id])

    for a in adjacencies:
        print(a[0], a[1])

if __name__ == "__main__":
    main()