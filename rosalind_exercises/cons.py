from util import exfasta

filepath = "./rosalind_data/rosalind_cons.txt"
dnadict = exfasta(filepath)
dnas = list(dnadict.values())

a_profile = []
c_profile = []
g_profile = []
t_profile = []

for i in range(len(dnas[0])):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for dna in dnas:
        if dna[i] == "A":
            a_count += 1
        elif dna[i] == "C":
            c_count += 1
        elif dna[i] == "G":
            g_count += 1
        elif dna[i] == "T":
            t_count += 1
    a_profile.insert(i, a_count)
    c_profile.insert(i, c_count)
    g_profile.insert(i, g_count)
    t_profile.insert(i, t_count)

profile = {}
nucleotide_profiles = [a_profile, c_profile, g_profile, t_profile]
nucleotides = ["A", "C", "G", "T"]
for i in range(len(nucleotides)):
    profile[nucleotides[i]] = nucleotide_profiles[i]

#print(profile)
#{'A': [5, 1, 0, 0, 5, 5, 0, 0], 'C': [0, 0, 1, 4, 2, 0, 6, 1], 'G': [1, 1, 6, 3, 0, 1, 0, 0], 'T': [1, 5, 0, 0, 0, 1, 1, 6]}

consensus = ""
for p in range(len(dnas[0])):
    max_frequency = 0
    most_frequent_base = ""
    for key, value in profile.items():
        if value[p] > max_frequency:
            max_frequency = value[p]
            most_frequent_base = key
    consensus += most_frequent_base

print(consensus)
for key, value in profile.items():
    print(key + ": " + ' '.join(str(x) for x in value))