i = int(input())

for n in range(1, i+1):
    ans = (n * n * ((n * n )- 1)) - 48 - 16 * (n - 4) - 24 * (n - 4) - (n - 4)**2 * 8
    print(ans//2)