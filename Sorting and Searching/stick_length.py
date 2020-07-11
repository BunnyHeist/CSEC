n = int(input())
ls = [int(i) for i in input().split()]

ls.sort()

mid = n // 2

ans = sum(ls[mid + n%2 :]) - sum(ls[:mid])

print(ans)