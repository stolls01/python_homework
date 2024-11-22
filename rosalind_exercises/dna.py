# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces)
# counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

s = "AGTCTAAAAAAA"
counter = {}

for letter in s:
    if letter not in counter:
        counter[letter] = 1
    else:
        counter[letter] += 1

print(counter["A"], counter["C"], counter["G"], counter["T"])




def count(s):
    counter = {}
    for letter in s:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1