import random , sys
user_score = 0
cp_score = 0
while True: 
  if(user_score == 3 or cp_score == 3):
    break
  user = input("\n\nPlease enter a number \n1.rock \n2.paper \n3.scissor \n")

  if(user.isdigit()==False):
      print(f"you must be enter 1 or 2 or 3 but you enter : {user}")
  if(user.isdigit()):
    user = int(user)
    if(user < 0 or user > 3):
      print(f"you must enter 1 or 2 or 3 but you enter : {user}")
      sys.exit()

    cp = random.choice("123")
    cp = int(cp)

    print(f"your choice : {user}\n cp choice : {cp}")
    print(f"user score : {user_score} \n cp_score :{cp_score}")
    if(user == 1 and cp == 3 ):
      print("you win")
      user_score += 1
     
    elif(user == 2 and cp == 1):
      print("you win")
      user_score += 1
    elif(user == 3 and cp == 2):
      print("you win")
      user_score += 1
    elif(user == cp):
      print("tie game")
    else :
       print("cp win")
       cp_score +=1
  