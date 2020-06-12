a = int(input())
b = [[int(i) for i in input().split()]for j in range(a)]

for i in range(a):
    v1, v2 = b[i][0], b[i][1]

    if v1 <= 2*v2 and v2 < 2*v1 and (v1+v2) % 3 ==0:
        print("YES")
    else:
        print("NO")
