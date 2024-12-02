from util import exfasta
filepath = "./rosalind_data/rosalind_lcsm.txt"
dnas = list(exfasta(filepath).values())

longest_string = ""
for d in dnas:
    if len(d) > len(longest_string):
        longest_string = d

longest_substring = ""

for x in range(0, (len(longest_string))):
    for y in range(len(longest_substring)+1, 1000-x):
        current_substring = longest_string[x:x+y] 
        if len(current_substring) > len(longest_substring):
            temp = ""
            for dna in dnas:
                if "STOP" in temp:
                    break
                elif current_substring in dna:
                    temp += ""
                else:
                    temp += "STOP"
            if "STOP" not in temp:
                longest_substring = current_substring
            else:
                pass

print(longest_substring)