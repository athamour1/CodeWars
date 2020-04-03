import math
def is_square(n):    
      if n > 0:
          return(int((math.sqrt(n)) + 0.5) ** 2 == n)
      elif n == 0:
          return True
      else:
          return False