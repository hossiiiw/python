from pathlib import Path
import os
import shutil


# p = Path("path\\docs\\test.txt")


# file = open(p , "r")

# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# for line in file :
#   print(line)

# file.close()

# file = open(p , "a")
# file.write("test\n")
# file.write("test\n")
 
# p = Path("path\\docs\\test2.txt")
# file = open(p , "a")
# file.write("First Sentance\n")


# if not os.path.exists(p):
#   file = open(p , "x")
# file.write("test")


# new = Path("path\\docs\\t.txt")

# if not os.path.exists(new):
#   newfile = open(new , "x")
#   newfile.write("Create new file")


my_path = Path("path\\docs\\test.txt")
my_path.write_text("test")
print(my_path.read_text())
if os.path.exists(my_path):
  os.remove(my_path)


copy_path = Path("path\\docs\\t.txt")
target = Path("path\\docs\\test2.txt")
target.write_text(copy_path.read_text())


shutil.copy(copy_path , target)

del_path = Path("path\\docs\\t.txt")
del_path.unlink()