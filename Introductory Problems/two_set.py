n = int(input())

a= set()
b = set()

su = n *(n+1) //2

if su % 2 == 0:
    print("Yes")

    for i in range(n,0,-1):
        if sum(a) > sum(b):
            b.add(i)
        else:
            a.add(i)
    print(len(a),*a,len(b),*b)

else:
    print("No")
