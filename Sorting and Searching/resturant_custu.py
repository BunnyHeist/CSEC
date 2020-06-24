n = int(input())

arrival = []
leave = []

for i in range(n):
    x, y = input().split()
    arrival.append(x)
    leave.append(y)

arrival.sort()
leave.sort()

ma = 0
current =0
i , j = 0,0

while i < n and j<n:
    if arrival[i] < leave[j]:
        current +=1
        i += 1
    else:
        current -=1
        j +=1

    if ma < current:
        ma = current


print(ma)