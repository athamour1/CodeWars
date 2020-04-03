def DecimalToBinary(num,binary):
  if num > 1:
    DecimalToBinary(num // 2,binary)
  binary.append(num % 2)   
  return num ,binary

def countBits(num):
  binary= []
  if num < 0:
    print("Wrong number")
  elif num == 0:
    return 0
  else:
    num, binary = DecimalToBinary(num, binary)
    #print(binary)
    x=len(binary)
    #print(x)
    k=0
    for i in range(x):
      if binary[i]==1:
        k=k+1
    return k