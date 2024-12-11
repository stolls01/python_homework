k = 17 # homo dominant
m = 27 # heterozygous
n = 20 # homo recessive
s = k + m + n

pr = k/s + m/s * ((4*k + (3*m-3) + 2*n)/(4*(s-1))) + n/s * ((2*k + m)/(2* (s - 1)))

print(pr)




# k and k: 100%
# k and m: 100%
# k and n: 100%

# m and m: 75%
# m and n: 50%
# m and k: 100%

# n and n: 0%
# n and k: 100%
# n and m: 50%