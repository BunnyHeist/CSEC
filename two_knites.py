i = int(input())

for n in range(1,i+1):
    ans = (n*n *((n*n)-1)) - 8 - 24 - 16 *(n-4) - 16 - 24 * (n-4) - (n-4)**2 * 8
    print(ans//2)