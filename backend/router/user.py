from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from models.user import User
from services.db import connect_mongo_db, insert_one_user, search_by_email
from services.auth import generate_jwt_token
from schemas.user import Response
from config.settings import constants
from services.file import create_base_structure

router = APIRouter()

connect_mongo_db()

@router.post("/login")
async def login(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        email = body["email"]
        password = body["password"]
        user_details = search_by_email(email)
        for i in user_details:
            if i.email == email and i.password == password:
                create_base_structure(email = email)
                jwt_token = generate_jwt_token(email = email, password = password)
                response = Response()
                response.jwt = str(jwt_token)
                response.message = constants.SUCCESS_LOGIN
                return JSONResponse(status_code=status.HTTP_200_OK, content=response.dict(exclude_none=True))
        else:
            response = Response()
            response.message = constants.INVALID_LOGIN
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=response.dict(exclude_none=True))
    except Exception as e:
        print(e)
        response = Response()
        response.message = constants.ERROR
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.dict(exclude_none=True))

@router.post("/signup")
async def singup(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        user_model = User(first_name = body["first_name"], last_name = body["last_name"], email = body["email"], password = body["password"])
        user_model.validate()
        insert_one_user(user_model)
        response = Response()
        response.message = constants.SUCCESS_SIGNUP
        return JSONResponse(status_code=status.HTTP_200_OK, content=response.dict(exclude_none=True))
    except Exception as e:
        print(e)
        response = Response()
        response.message = constants.ERROR
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.dict(exclude_none=True))