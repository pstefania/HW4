s = 'GGAGAGTAGTCACTTAGAGTAGGATACTAGAGTAGAGAGTAGAGAGTAGGACCCCAAGAGTAGAAGAGTAGAAGAGTAGCCAGAGTAGAGAGTAGCAGAGTAGCCCGCAGAGTAGAGAGTAGTAGAGTAGCAGAGTAGCAGAGTAGTAGAGTAGGTAGAGTAGGTGCCAGAGTAGCCCCAGAGTAGAGAGTAGGAGAGTAGTCAGAGTAGGTAGAGTAGGTTTTTAGAGTAGCAGAGTAGAAGAGTAGCCTGTAAGAGTAGTGGGCGTAATAGAGAGTAGTTGGTGCAGAGTAGTATAGAGTAGTAGAGTAGTAGAGTAGCTTTATCCTAAAGAGTAGCAGAGTAGGGTTTGTTAGAGTAGAAGAGTAGCGATTTCGAGGACGAGAGTAGGCCAGAGTAGCCTCGCAATTAGAGTAGAGAGTAGAGAGTAGAGAGTAGCGAGAGTAGAGGTGGCAGAGTAGCCTGTTCCAGAGTAGAGAGTAGAGAGTAGAGAGTAGAGAGTAGCGTTAGAGTAGCAGAGTAGCGACAGAGTAGAGAGTAGGACAGATAGAGTAGCTTATTAGAGTAGAGAGTAGAAGAGTAGGACTAGAGTAGTACAGAGTAGAGAGTAGTCGAGAGTAGAGAGTAGTTAGAGTAGTAGTTGAGAGTAGAGAGTAGTAGAGTAGAAGAGTAGTTAAGAGTAGAGAGTAGTATATAGAGTAGAGAGTAGCGTTAGAGTAGGAAGAGTAGGACGAGAGTAGACCCAGAGTAGTAGTAGAGTAGCAGAGTAGAGAGTAGAGAGTAGGCAGAGTAGTTAGAGTAGAGAGTAGTTGAGAGTAGGTAGAGAGTAGGCTAGAGTAGACGAGTTAGAGTAGTACAAGAGTAGTTTGTTGTATTCGCCAGAGTAGCCTTCTGAGAGTAGAGAGTAGGAAGAGTAGGAGAGTAGCTGGAAAAGAGTAGAAAGAGTAGAGAGTAGCAGAGTAGAGAGTAGAGAGTAGGTCAGAGTAG'
t = 'AGAGTAGAG'
inds = []
for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        inds.append(i+1)
for i in inds:
    print (i)
