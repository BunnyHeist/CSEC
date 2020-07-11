from bisect import bisect_right

n = int(input())
ls = [int(i) for i in input().split()]

l = []
total_ans = 0

for i in ls:
     pos = bisect_right(l,i)
     if pos >= total_ans:
         l += [i]
         total_ans += 1
     else:
        l[pos] = i
print(total_ans)