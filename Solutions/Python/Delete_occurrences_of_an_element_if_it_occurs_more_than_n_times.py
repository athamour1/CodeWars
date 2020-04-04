def delete_nth(o, e):
    if not o or e < 1:
        return[]
    x = { i:0 for i in o }
    y = []
    
    for i in o:
        if x[i] < e:
            x[i] = x[i] + 1
            y.append(i)
    return y
