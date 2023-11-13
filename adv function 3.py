def salesrep (lastname, sales):
  if (sales >100000): 
    comission= .10*sales
  else:
    comission=.05*sales
  target=.05*sales
sales=int(input ("enter sales"))
lastname=(input("enter last name")) 
salesrep(lastname, sales)
