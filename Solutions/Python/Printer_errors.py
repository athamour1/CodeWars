A='abcdefghijklm'

def printer_error(s):
    x=len(s)
    #print(x)
    k=0
    for i in range(x):
      for j in range(13):
           #print(A[j])
           if s[i] == A[j]:
               k=k+1
      #print(k)
    k=x-k
    return(str(k) + '/' + str(x))