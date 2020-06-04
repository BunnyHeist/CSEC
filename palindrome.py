a = input()
ls = sorted(list(set(a)))
m=''
half = ""
x=0

for i in ls:
    n = a.count(i)
    if n % 2 == 0:
        half += i * (n//2)

    elif x==1:
        half = 0
        print("NO SOLUTION")
        break

    else:
        x = 1
        m = i
        half += i * ((n-1)//2)


if half != 0:
    print(half + m + half[::-1])