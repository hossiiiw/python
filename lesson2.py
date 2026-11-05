
names = ["hossein" , "asra" , "sana" ]
courses=  ["py" , "js" , "java"]
number = 10


# for count in range(10):
#   password = input("enter ypur password : ")
#   if(password == "hossein"):
#     break
# print("for ended")


# for name in names :
#   for course in courses :
#     print(f"{name} : {courses}")


# while number >= 1 :
#   user =input("enter sth :")
#   if(user == "2"):
#     break
#   number   -=1


user_input = ""
while user_input != "end":
  user_input = input(">>")
  if(user_input == "s"):
    continue
  print(user_input)