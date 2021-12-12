from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_cors import CORS
from models.user import User



#curl -X POST http://127.0.0.1:5000/auth  -H "Content-Type: application/json" -d '{ "username": "test1@email.com", "password": "11111" }'
def authenticate(username, password):
    user = User.get("email", username)
    user_password = user.hash
    if user and safe_str_cmp(user_password.encode("utf-8"), password.encode("utf-8")):
        return user


def identity(payload):
   user_id = payload["identity"]
   user = User.get("id", user_id)
   return user if user else None


app = Flask(__name__)
CORS(app)
app.debug = True
app.config["SECRET_KEY"] = "super-secret"
jwt = JWT(app, authenticate, identity)


# curl -X POST http://127.0.0.1:5000/api/signup -d '{"first":"Alex", "last":"Castro", "password":"11111", "email":"test1@email.com"}' -H "Content-Type: application/json"
@app.route("/api/signup" , methods=["POST"])
def signup():
    data = request.get_json()
    first = data.get("first")
    last = data.get("last")
    email = data.get("email")
    password = data.get("password")
    new_user = User(email=email, first=first, last=last, hash=password)
    new_user.insert()
    user = User.get("email", email)
    id = user.id
    return jsonify({"status":"success", "id":id})


#curl http://127.0.0.1:5000/protected -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzkyNjcxNzYsImlhdCI6MTYzOTI2Njg3NiwibmJmIjoxNjM5MjY2ODc2LCJpZGVudGl0eSI6MX0.CCtQVACkW7Il7oeHuypPQbI8Jl93CgCeYmXDslJiZhA" 
@app.route("/protected")
@jwt_required()
def protected():
    return jsonify({"status":"success", "id":current_identity.id})


