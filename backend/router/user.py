from fastapi import APIRouter, Request, status
import jwt
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

from models.user import User
from services.db import connect_mongo_db, insert_one, search_by_email, check_user_data
from config.settings import jwt_setting
from schemas.user import Response

router = APIRouter()

connect_mongo_db()

def check_jwt_token(jwt_token : str) -> int:
    """Validate JWT Token

    Args:
        jwt_token (String): Jwt Token as a String

    Returns:
        Int: 100 = Token is Valid and user is authenticated.
              101 = Token is Expired.
              102 = Token is Valid and not expired but password may changed
    """
    decoded = jwt.decode(jwt_token, jwt_setting.JWT_Secret, algorithms=["HS256"])
    current_time = str(datetime.now())
    remaining_time = (datetime.strptime(decoded["expiration"], jwt_setting.FMT) - datetime.strptime(current_time, jwt_setting.FMT)).total_seconds()
    if remaining_time > 0:
        return check_user_data(email = decoded["email"], password = decoded["password"])
    else:
        return 101

@router.post("/login")
async def login(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        email = body["email"]
        password = body["password"]
        #user_details = User.objects(email = email)
        user_details = search_by_email(email)
        for i in user_details:
            if i.email == email and i.password == password:
                jwt_token = jwt.encode({
                    "email" : email,
                    "password" : password,
                    "expiration" : str(datetime.now() + timedelta(seconds=jwt_setting.JWT_Expiry_Time))
                }, jwt_setting.JWT_Secret)
                response = Response()
                response.jwt = str(jwt_token)
                response.message = "Successfully Logged In"
                return JSONResponse(status_code=status.HTTP_200_OK, content=response.dict(exclude_none=True))
        else:
            response = Response()
            response.message = "Invalid Login!"
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=response.dict(exclude_none=True))
    except Exception as e:
        print(e)
        response = Response()
        response.message = "Error Occured. Please Try again leter!"
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.dict(exclude_none=True))

@router.post("/signup")
async def singup(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        user_model = User(first_name = body["first_name"], last_name = body["last_name"], email = body["email"], password = body["password"])
        user_model.validate()
        #user_model.save()
        insert_one(user_model)
        response = Response()
        response.message = "Successfully Singed Up!"
        return JSONResponse(status_code=status.HTTP_200_OK, content=response.dict(exclude_none=True))
    except Exception as e:
        print(e)
        response = Response()
        response.message = "Error Occured. Please Try again leter!"
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.dict(exclude_none=True))