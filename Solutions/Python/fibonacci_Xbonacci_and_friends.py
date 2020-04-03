def Xbonacci(si,n):
    x = si[:]
    
    for i in range(n-len(si)):
        k = 0
        top = len(x) - len(si)
        for j in x[top:]:
            k = k + j
        x.append(k)
    return x[:n]