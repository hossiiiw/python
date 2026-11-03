import json
from pathlib import Path


course = [
  {"id" : 1 , "name" : "hossein" , "salary" : 2000 },
  {"id" : 1 , "name" : "hossein" , "salary" : 2000 },
  {"id" : 1 , "name" : "hossein" , "salary" : 2000 }
]


data = json.dumps(course)
path = Path("path\\docs\\data.json").write_text(data)
read_data = Path("path\\docs\\data.json").read_text()
print(json.loads(read_data))
print(read_data)