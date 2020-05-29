n = int(input())

if n == 1:
    print(n)
elif n <4:
    print("NO SOlUTION")

else:
    for i in range(2,n+1,2):
        print(i)
    for i in range(1,n+1,2):
        print(i)