#n = months
#k = litter

def rabbits(n, k):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return rabbits(n-1, k) + k * rabbits(n-2, k)

n = 29
k = 2
print(rabbits(n, k))