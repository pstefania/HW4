def reverse_complement(s):
    complements = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

    sc = reversed(s)
    sc = [complements[c] for c in sc]

    return ''.join(sc)