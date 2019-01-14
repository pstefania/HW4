def translate(s):
    codontable = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
                  'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
                  'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP',
                  'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W',
                  'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                  'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                  'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                  'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                  'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
                  'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                  'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                  'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                  'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                  'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                  'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                  'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', }

    out = []

    protein = ''
    start = s.find('AUG')
    # translated region(tr)
    tr = s[start:]
    for n in range(0, len(tr), 3):
        if tr[n:n + 3] in codontable:


            if codontable[tr[n:n + 3]] == 'STOP':
                out.append(protein)
                protein = ''
            

            else:
                protein += codontable[tr[n:n + 3]]
    return out
print (translate(''))