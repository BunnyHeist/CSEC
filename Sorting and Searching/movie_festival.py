n = int(input())

ls = [[int(i) for i in input().split()] for _ in range(n)]

ls.sort(key= lambda x:x[1])
current_end_time = 0
movie = 0

for start,end in ls:
    if start >= current_end_time:
        movie += 1
        current_end_time = end

print(movie)

Instagram :