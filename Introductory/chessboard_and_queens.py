N = 8
col = N * [False]
diag_l = ((2 * N) - 1) * [False]
diag_r = ((2 * N) - 1) * [False]
reserved = [[c == '*' for c in input()]for _ in range(8)]
global count
count = 0

def check_next(r):
    global count
    if r == N :
        count += 1
        return


    for c in range(0,N):
        if(col[c] == False and diag_l[r - c + N - 1] == False and diag_r[r + c] == False and reserved[c][r] == False):
            col[c] = diag_l[r - c + N - 1] = diag_r[r + c] = True
            check_next(r + 1)
            col[c] = diag_l[r - c + N - 1] = diag_r[r + c] = False
    
    return count

x = check_next(0)
print(x)
