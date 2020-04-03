def tribonacci(si, n):
    if n == 0:
        return []
    if n < 3:
        return [si[i] for i in range(0,n)]
    x = si[:]
    for i in range(3,n):
        x.append(x[i-1] + x[i-2] + x[i-3])
    return x