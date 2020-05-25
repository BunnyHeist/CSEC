from sys import stdin

a = int(input(""))

c = {int(i) for i in stdin.readline().split()}


for x in range(1,a+1):
    if x in c:
        None
    else:
        print(x)


# n=int(input())
# print(n*(n+1)//2 - sum([int(i) for i in input().split()]))
