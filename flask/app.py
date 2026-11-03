from flask import Flask , jsonify , request 
from flask_cors import CORS



users = [
  {"id" : 1 , "name" : "Hossein" , "age": 25},
  {"id" : 2 , "name" : "Asra" , "age": 16},
  {"id" : 3 , "name" : "Sana" , "age": 13},
]


app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
  return "Wellcome to my first rest api"


@app.route("/api/users")
def get_users():
  return jsonify(users)


@app.route("/api/users/<int:user_id>" , methods=["GET"])
def get_user(user_id):
  for user in users :
    if user["id"] == user_id:
      return user
  else :
    return jsonify({"message" : "user not found" } ), 404





@app.route("/api/users" , methods=["PUT"])
def insert_user():
  data = request.get_json()
  new_user = {
    "id" : len(users)+ 1,
    "name" :  data.get("name"),
    "age" : data.get("age")
  }
  users.append(new_user)
  return jsonify(new_user)

@app.route("/api/users" , methods=["POST"])
def edit_user(user_id):
  data = request.json()
  for user in users:
    if user["id"] == user_id:
      user["name"] = data.get("name")
      user["age"] = data.get("age")
      return jsonify(user)

  else : jsonify({"message" : "user not found"}) , 404


@app.route("/api/users/<int:user_id>" , methods=["DELETE"])
def delete_user(user_id):
  global users
  users = [user for user in users if user["id"] != user_id]
  return jsonify({"message" : "user deleted"}) , 200



if __name__ == "__main__":
  app.run(debug=True)