def calculations(score1, score2, score3): 
  avg= (score1+score2+score3)/3
  totalpoints= score1+score2+score3

  return avg, totalpoints
  


lastname = (input("enterlastname"))
score1 = int(input("enter, score 1"))
score2 = int(input("enter score 2"))
score3 = int(input("enter score 3"))

output=calculations (score1, score2, score3)

print (output)