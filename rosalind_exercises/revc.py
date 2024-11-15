# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement of s.

# complement function
def comp(x):
    if x == "A":
        x = "T"
    elif x == "C":
        x = "G"
    elif x == "G":
        x = "C"
    elif x == "T":
        x = "A"
    return(x)

# adds each complement into u list
t = "GTAAGTC"
u = []
for p in range(len(t)):
	u.append(comp(t[p]))

# concatenates u into string, reverses and prints it
u = "".join(u)
print(u[::-1])