n = int(input())
ls = [int(i) for i in input().split()]

s = set() #empty set
j = 0
count = 0

for i in range(n):
    while ls[i] in s:
        s.remove(ls[j])
        j += 1
    s.add(ls[i])
    count = max(count, len(s))

print(count)