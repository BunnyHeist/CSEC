from itertools import permutations
n = input()

ls = sorted([''.join(i) for i in list(set(permutations(n)))])

print(len(ls), *ls)