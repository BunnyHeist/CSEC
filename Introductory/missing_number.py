n = int(input())
ls = [int(i) for i in input().split()]

print((n * (n+1)) // 2 - sum(ls))