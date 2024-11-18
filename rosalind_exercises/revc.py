# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement of s.

# complement function
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

t = "GTAAGTC"
reverse_complement(t)