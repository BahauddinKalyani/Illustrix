"""
Doc String

"""

from datetime import datetime, timedelta
from fastapi import FastAPI, Request
import pymongo
import uvicorn
import jwt
from .services.db import connect_mongo_db

app = FastAPI()

connect_mongo_db()

# @app.get('/first')
# def first():
#     return {"first": 1}

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["Illustrix"]
# user_table = mydb["user"]
# app = FastAPI()

JWT_SECRET = "Femj4ul1V2Xk3A3Amy6w7cE9gVAdn96Y"

FMT = '%Y-%m-%d %H:%M:%S.%f'

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/check_jwt_token")
async def check_jwt_token(request: Request):
    try:
        body = await request.json()
        jwt_token = body["jwt"]
        decoded = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"])
        current_time = str(datetime.now())
        print(decoded)
        remaining_time = (datetime.strptime(decoded["expiration"], FMT) - datetime.strptime(current_time, FMT)).total_seconds()
        if remaining_time > 0:
            return {"Status" : 200, "Remaining Time" : remaining_time, "Data" : decoded}
        else:
            return {"Status" : 101, "Remaining Time" : remaining_time, "Data" : decoded}
    except Exception as e:
        return {"status" : 400, "message" : str(e)}

@app.post("/login")
async def login(request: Request):
    try:
        body = await request.json()
        email = body["email"]
        password = body["password"]
        query = { "email": email }
        res = user_table.find(query)
        for i in res:
            if i["email"] == email and i["password"] == password:
                jwt_token = jwt.encode({
                    "email" : email,
                    "password" : password,
                    "expiration" : str(datetime.now() + timedelta(seconds=600))
                }, JWT_SECRET)
                return {"status" : 200, "message" : "Successfully Logged In", "id" : str(i["_id"]), "jwt" : str(jwt_token)}
        else:
            return {"status" : 200, "message" : "Invalid Login!"}
    except Exception as e:
        return {"status" : 400, "message" : str(e)}

@app.post("/signup")
async def singup(request: Request):
    try:
        body = await request.json()
        print(body)
        insert_into_user_table = user_table.insert_one(body)
        return {"id" : str(insert_into_user_table.inserted_id), "status" : 200, "message" : "Successfully Singed Up!"}
    except Exception as e:
        return {"status" : 400, "message" : str(e)}

if __name__ == "__main__":
    uvicorn.run("Server:app", host="localhost", port=8000,reload=True)