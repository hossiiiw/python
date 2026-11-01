import random , sys

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

  if(user == 1 and cp == 3 ):
    print("you win")
  elif(user == 2 and cp == 1):
    print("you win")
  elif(user == 3 and cp == 2):
    print("you win")
  elif(user == cp):
    print("tie game")
  else : print("cp win")