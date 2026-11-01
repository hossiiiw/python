


def wellcome (name = "x"):
  print(f"wellcome to app {name}")

# wellcome("hossein")
# wellcome("asra")




def get_freeting():
  return "hello"
# test = get_freeting()
# print(test) 





def sum (x=0, y=0) :
  value = x + y
  return value
# print(sum(2 , 4))



def multiply(*number) :
  result = 1
  for i in number :
      result = result * i
  return result

# print(multiply(1,3,3,5,4,8))



def multyply_xx(**data):
  print(data)
  print(type(data))
  print(data["name"])
  print("===========")
  for i in data :
    print(i , data[i])
# multyply_xx(name="test" , age = "25")


def add_one(num) :
    if(num >= 10):
       return num
    total = num + 1
    print(total)
    return add_one(total) 

# add_one(0)



name = "global name"

def name1 ():
   name = "name1"
   print(name)


def name2 ():
   global name
   name = "chnage name"

# name1()
# name2()
# print(name)


  

def func1 ():
  name = "hossein"
  def func2():
    nonlocal name
    name = "imani"
  func2()
  return name


# print(func1())


 
def parent_func (player):
   coins = 3

   def play_game():
      nonlocal coins
      coins -= 1
      if(coins < 0):
        print(f"{player} do not have chance")
        return
      print(f"{player} has {coins} left")


   return play_game


user1 = parent_func("hossein")
user2 = parent_func("asra")
user1()
user1()
user2()
user1()
user1()
