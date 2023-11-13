quant=int(input("enter quantity"))
unitprice=int(input("enter unit price"))

def computeTotal ():
  total=quant*unitprice
  total=total+ (total *.07)
  return total

output= computeTotal ()

print ("total", output)
print ("tax" , "0.07")