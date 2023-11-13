def CalcDiscount(quantity,price,discountrate):

  totalprice= quantity*price
  discounted= totalprice *discountrate
  discountedprice= totalprice-discounted

  return discounted, discountedprice


quantity = int(input("enter quant"))
price = int(input("enter price"))
discountrate= float (input("enter discount rate"))

output=CalcDiscount(quantity, price, discountrate)

print("quantity", quantity)
print("price", price)
print ("Discounted amount and discounted price" , output)
