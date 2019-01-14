def count_basie(s):
    counted = {}
    ordered = []

    for c in s:
        if not counted.has_key(c):
            counted[c] = 0
        counted[c] += 1

    for c in sorted(counted.iterkeys()):
        ordered.append(counted[c])

    return ordered