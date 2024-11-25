months = 25
fertile = 0
litter = 5
unfertile = 1

# rn = rn-1 + rn-2 * litter

for i in range(months):
    new_gen = fertile + unfertile
    print(new_gen)
    # with next month/iteration, all unfertile + fertile ones (= this new generation) will be fertile
    fertile = new_gen
    unfertile = fertile * litter
