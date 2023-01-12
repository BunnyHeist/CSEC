n = int(input())
ls = sorted([int(i) for i in input().split()])

s1 = set()
s2 = set()

for x in range(len(ls) - 1, -1, -1):
    if sum(s1) <= sum(s2):
        s1.add(ls[x])
    else:
        s2.add(ls[x])

print(abs(sum(s1) - sum(s2)))