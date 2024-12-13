from util import exfasta

filepath = "test.txt"
dnadict = exfasta(filepath)

def main():
    adjacencies = []
    for identifier, dna in dnadict.items():
        k = 3
        for id, dna_2 in dnadict.items():
            if identifier == id:
                continue
            if dna == dna_2:
                continue
            if dna[len(dna)-k:] == dna_2[:k]:
                adjacencies.append([identifier, id])
                # adjacencies.append([flipped_dna[:k], dna_2[:k]])

    # print(adjacencies)
    for a in adjacencies:
        print(a[0], a[1])

if __name__ == "__main__":
    main()