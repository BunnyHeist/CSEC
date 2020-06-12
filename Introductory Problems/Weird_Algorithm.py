n = int(input())

print(n)

while n!=1: # until n becomes 1 
    
    if n%2 == 0: 3 #if n is even
       
        n = n //2
        print(n)
    
    else: # if n is odd
       
        n = n*3 +1
        print(n)
