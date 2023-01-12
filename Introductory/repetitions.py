ls = list(input())

lc = 0
mc = 0

for i in range(1, len(ls)):
    if ls[i] == ls[i-1]:
        lc += 1
        if lc >= mc:
            mc = lc
    else:
        lc = 0
print(mc + 1)