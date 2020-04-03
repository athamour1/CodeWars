def likes(names):
    x=len(names)
    if x == 0:
        return('no one likes this')
    elif x == 1:
        return(names[0] + ' likes this')
    elif x == 2:
        return(names[0] + ' and ' +names[1] + ' like this')
    elif x == 3:
        return(names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')
    else:
        x = x - 2
        return(names[0] + ', ' + names[1] + ' and ' + str(x) + ' others like this')