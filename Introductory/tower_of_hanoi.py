n = int(input())
print(2**n - 1)


def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print(source, destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print(source, destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

TowerOfHanoi(n,'1','3','2')
