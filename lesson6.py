 

sum = lambda num1 , num2 : num1 + num2
# result = sum(2, 4)
# print(result)


def function_bulder(x):
  return lambda y : y + x

add = function_bulder(20)
# print(add(24.5))

  

classes_score = [
  ("hossein" , 10),
  ("asra" , 20),
  ("sana" , 15),
  ("ali" , 5)
]


classes_score.sort()
# print(classes_score)

classes_score.sort(key=lambda items : items[1])
classes_score.reverse()
# print(classes_score)



newlist = map(lambda item : (item[0] , item[1] > 10) , classes_score)
# print(list(newlist))

filterlist =filter(lambda item : item[1] > 5 , classes_score)
# print(list(filterlist))


result = [(item[0] , item[1] > 10 ) for item in classes_score]
# print(result)

result2 = [item for item in classes_score if item[1] > 10]
# print(result2)


nums = [1,2,3,4,5,6,7,8,9,10]

odd_num = [number for number in nums if number % 2 != 0 ]
# print(odd_num)
lower5 = [number**5 for number in nums if number <= 5]
# print(lower5)

tavan2 = [number**2 if number % 2 == 0 else number for number in nums]
# print(tavan2)


ex_list =[
  {
    "name" : "hossein",
    "score"  : 10
  },
  {
    "name" : "asra",
    "score"  : 23
  },
  {
    "name" : "sana",
    "score"  : 25
  },
 ]


exlist_test = [item for item in ex_list if item["score"] > 10]
# print(exlist_test)


# print([{"name" : x["name"] , "passed" : x["score"] >=10} for x in ex_list])



# Exceptions - Error handeling
courses = ["html" , "css"]
print("\n\n\n")

try :
  file = open("lesson1.py")
  age = int(input("enter your age : "))
  if age < 10 : 
    raise Exception("Invalid age")
  x = 2 / age
  print(courses[1])
# except IndexError :
#   print("this is an index error")
# except ValueError :
#   print("this is an value error")
# except ZeroDivisionError :
#   print("you can not devide 0") 
except Exception as error: 
  print(f"an error raised : {error}")
  print(type(error))

else : 
  print("thanks")
finally :
  file.close()
  

print("-----------app is finished------------") 