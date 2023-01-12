n = int(input())

ls1, ls2 = set(), set()

su = n *(n+1) //2


if su % 2 == 0:
    print("YES")
    hal = su//2
    for i in range(n,0,-1):
        if i <= hal:
            ls1.add(i)
            hal -= i
        else:
            ls2.add(i)
    print(len(ls1),*ls1,len(ls2),*ls2)
else:
    print("NO")