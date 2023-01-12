def gray_code(n = int(input())):
    if n == 0:
        return []
    if n == 1:
        return ['0', '1']
    gray = gray_code(n-1)
    return ['0' + s for s in gray] + ['1' + s for s in reversed(gray)]
 
print("\n".join(gray_code()))