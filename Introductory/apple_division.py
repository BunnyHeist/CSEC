n = int(input())
ls = sorted([int(i) for i in input().split()])

def find_min(ind, box_1, box_2):
    if ind == n:
        return abs(box_1 - box_2)
    else:
        return(min(find_min(ind + 1, box_1 + ls[ind], box_2),find_min(ind + 1, box_1, box_2 + ls[ind])))

print(find_min(0,0,0))