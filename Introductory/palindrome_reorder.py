n = input()
ls = sorted(set(n))

half = ''
flag = 0
m = ''

for i in ls:
    x = n.count(i)
    if x % 2 == 0:
        half += i * (x//2)
    else:
        flag += 1
        if flag < 2:
            m = i
            half += i * (x//2)
        else:
            print("NO SOLUTION")
            break

if flag < 2:
    print(half + m + half[::-1])
