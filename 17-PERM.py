
from itertools import permutations

def permutation(n):

    count = 0
    variable = list (permutations(range(1,n+1)))

    for i in variable:
        count += 1
    print(count)

    for i in variable:
        print(' '.join(map(str,i)))