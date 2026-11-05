import csv

with open("path\\docs\\data.csv" , "w",newline="", encoding="utf-8" ) as file :
  writer = csv.writer(file)
  writer.writerow([" id " , " name " , " salary "])
  writer.writerow([1 , " Hossein " , 2500 ])
  writer.writerow([2 , " Asra " , 3500])
  writer.writerow([3 , " Sana " , 300])


with open("path\\docs\\data2.csv" , "w" , newline="") as file :
  writer = csv.writer(file)
  writer.writerow([" id " , " name " , " salary "])
  writer.writerow([1 , " Hossein " , 2500 ])
  writer.writerow([2 , " Asra " , 3500])
  writer.writerow([3 , " Sana " , 300])
  writer.writerow([10 , "Ali" , 300])


with open("path\\docs\\data.csv" ) as file :
  reader = csv.reader(file)
  for row in reader : 
    print(row)

with open("path\\docs\\data2.csv") as file :
  reader = csv.reader(file)
  for row in reader :
    print(row)