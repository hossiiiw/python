import json
from pathlib import Path


course = [
  {"id" : 1 , "name" : "hossein" , "salary" : 2000 },
  {"id" : 1 , "name" : "hossein" , "salary" : 2000 },
  {"id" : 1 , "name" : "hossein" , "salary" : 2000 }
]


data = json.dumps(course)
new_path = Path("path\\docs\\newdata.json").write_text(data)
path = Path("path\\docs\\data.json").write_text(data)
read_data = Path("path\\docs\\data.json").read_text()
courses= json.loads(read_data)
print(courses[0])

