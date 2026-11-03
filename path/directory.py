from pathlib import Path
import os

# p = Path("path\\docs")
# if not p.exists():
#   p.mkdir()
# p.rmdir()
 
# os.mkdir("path\\docs")
# os.rmdir("path\\docs")

content = os.listdir("..\\python")
content = os.listdir(Path())
print(content)