wochen = 29
reife = 1
unreife = 0
litter = 5

for i in list(range(wochen-1)):
    neue_gen = reife + unreife * litter
    #A MONTH PASSES AND UNRIPE ONES WILL NOW BE RIPE
    unreife = reife
    reife = neue_gen
    print(neue_gen)