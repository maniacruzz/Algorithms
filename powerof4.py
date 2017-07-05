def power4(num):
  if num==1 or (str(num)[-1] in ['6','4'] and num&(num-1)==0):
    return True
  return False
  
for i in [-10,4,1,16,32,256]:
  print(i,power4(i))