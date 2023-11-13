def calculations(s1, s2, s3, h):
  average = (s1 + s2 + s3) / 3
  averagewh = (s1 + h + s2 + h + s3 + h) / 3

  return average, averagewh

lastname = input("Enter last name: ")
handicap = int(input("Enter handicap: "))

score1= int(input("Enter score 1"))
score2= int(input("Enter score 2"))
score3= int(input("Enter score 3"))

Output=calculations(score1, score2, score3, handicap)

print ("last name", last name)
print( "average score and average handicap score ", output )