from itertools import permutations
a = input()

ls = sorted([''.join(i) for i in list(set(permutations(a)))])

print(len(ls))
for i in ls:
    print(i)