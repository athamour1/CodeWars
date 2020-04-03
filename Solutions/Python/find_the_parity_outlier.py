def find_outlier(o):
    x=len(o)
    k = l = 0
    for i in range(x):
        if o[i]%2 is 0:
            k = k + 1
        else:
            l = l + 1
    if k is 1:
        for i in range(x):
            if o[i]%2 is 0:
                return(o[i])   
    elif l is 1:
        for i in range(x):
            if not(o[i]%2 is 0):
                return(o[i]) 