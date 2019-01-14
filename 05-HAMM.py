def hamming_distance(s, t):
    dh = 0

    for i, c in enumerate(s):
        if c != t[i]:
            dh += 1

    return dh