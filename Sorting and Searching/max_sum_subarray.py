n = int(input())
ls = [int(i) for i in input().split()]

local_max = 0
overall_all = ls[0]

for i in range(n):
    local_max = max(ls[i],local_max + ls[i])
    overall_all = max(local_max,overall_all)

print(overall_all)