# zero = [0] *50
# print(zero)

# number = list(range(0 , 50))
# print(number)


names = ["hossein" , "asra" , "sana" , "hasan" , "zeynab" , "ali"]
names[2] = "z"
names.append("test")
print(names)

names[3:3] = ["1" , "2" , "5"]
print(names)
names[3:6] = ["1" , "2" , "5" , "5" , "5"]
print(names)


names.pop()
print(names)

names.remove("2")
print(names)

# del names[4 : 7]

print(names)

# names.clear()
# print(names)
# del names

print(names.index("5"))
print(names.count("asra"))
print(names.count("5"))


for i in names : 
  print(i)

for i , j in enumerate(names):
  print(i , j)

names.sort()
print(names)

names.append("Hossein")
names.sort(key=str.lower)
print(names)


number = [2 , 1 , 5 , 20 ,10 ]
print(number)
number.sort()
print(number)
number.reverse()
print(number)

# test =sorted(number)
# print(test)

copy_list = number.copy()
print(copy_list)
copy_list3 = number
number[0] = 100
copy_list2 = list(number)
print(copy_list2 , copy_list3)


copy_list4 = number[:]
print(copy_list4)
