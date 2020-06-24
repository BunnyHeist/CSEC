n, x = input().split()
ls = [int(i) for i in input().split()]

x = int(x)
temp = {}

for i in range(int(n)):
    p = ls[i]
    if x - p in temp:
        print(i +1, temp[x - p] + 1)
        quit()
    else:
        temp[p] = i

print("IMPOSSIBLE")