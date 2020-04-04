sol = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print2d(x): #δισδιαστατη εκτυπωση
  n = len(x)
  m = len(x[0])
  for i in range(n):
    print("|", end = "")
    for j in range(m):
      print(x[i][j], end ="\t|")
    print("\t")
  
def valid_solution(b):
    print2d(b)
    for i in range(9):
        o = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            for z in range(9):
                if b[i][j] == sol[z]:
                    o[z] = 1
        for j in range(9):
            if o[j] == 0:
                return False
    for i in range(9):
        o = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            for z in range(9):
                if b[j][i] == sol[z]:
                    o[z] = 1
        for j in range(9):
            if o[j] == 0:
                return False
    for i in range(3):
        for j in range(3):
            g = 0
            for k in range(3):
                for l in range(3):
                    g = g + b[i*3+k][j*3+l]
                    if b[i][j] < 1 or b[i][j] > 9:
                        print (3)
                        return False
            if g != 45:
                return False
    return True