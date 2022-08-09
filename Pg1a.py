import math
number = int(input("enter n:"))
rows = number
cols = math.ceil(number/2)
for i in range (1,rows+1):
  for n in range (1,cols+1):
    if(n==1 or i==n or  (i+n==number+1)):
      print("*",end="\t")
    else:
      print(" ",end = "\t")
  print(" ")
