n = int(input())
ls = []
for i in range(n):
    ls.append([int(i) for i in input().split()])

for i in range(n):
    x,y = ls[i][0], ls[i][1]

    if x > y:
        if x % 2 == 0:
            print(x * x - y + 1)
        else:
            x -= 1
            print(x * x + y)
    else:
        if y % 2 == 1:
            print(y * y - x + 1)
        else:
            y -= 1
            print(y * y + x)
