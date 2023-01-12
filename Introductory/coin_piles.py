n = int(input())
ls = [[int(i) for i in input().split()] for x in range(n)]

for i in range(n):
    x, y = ls[i][0], ls[i][1]

    if 2 * x >= y and 2 * y >= x and (x + y) % 3 == 0:
        print('YES')
    else:
        print('NO')