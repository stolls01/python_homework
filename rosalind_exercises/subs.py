def comb(s, t):
    o = []
    for x in range(len(s)):
        if s[x:x+len(t)] == t:
            o.append(x + 1) # +1 for human-readable lines
    return(o) # list of occurrences (positions)

s = "GATATATGCATATACTT"
t = "ATAT"

result = comb(s, t)
print(" ".join(str(x) for x in result)) # need to convert integers into strings to join them