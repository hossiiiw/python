from zipfile import ZipFile
from pathlib import Path

with ZipFile("path\\zip1.zip" , "w") as zip:
  for path in Path("path\\docs").rglob("*.*"):
    zip.write(path)


with ZipFile("path\\zip1.zip" , "r") as zip:
   print(zip.namelist())
   zip.extractall("path\\extract")