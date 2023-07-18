from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from schemas.image import Response
from config.settings import constants
from services.file import get_file_path_from_url
from services.db import connect_mongo_db, insert_or_update_user_image
from services.auth import get_jwt_token, check_jwt_token, get_user_data_by_jwt
from services.ml_services.background_remove import background_remove_fun
from services.ml_services.self_background_blur import self_background_blur_fun
from services.ml_services.background_remove_and_blur import background_remove_and_blur_fun

router = APIRouter()

connect_mongo_db()

@router.post("/background_remove")
async def background_remove(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        jwt_token = get_jwt_token(request)
        validate_jwt_token = check_jwt_token(jwt_token)
        if validate_jwt_token == 100:
            user_details = get_user_data_by_jwt(jwt_token)
            file_name, system_file_path, global_url, background_url = get_file_path_from_url(body)
            bg_remove = background_remove_fun(file_name, system_file_path)
            insert_or_update_user_image(file_name = file_name, email = user_details["email"], url = global_url)
            response = Response()
            response.message = constants.SUCCESSFULLY_PERFORMED
            response.url = global_url
            return JSONResponse(status_code=status.HTTP_200_OK, content=response.dict(exclude_none=True))
        elif validate_jwt_token == 101 or validate_jwt_token == 102:
            response = Response()
            response.message = constants.INVALID_LOGIN
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=response.dict(exclude_none=True))
    except Exception as e:
        print(e)
        response = Response()
        response.message = constants.ERROR
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.dict(exclude_none=True))

@router.post("/self_background_blur")
async def self_background_blur(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        jwt_token = get_jwt_token(request)
        validate_jwt_token = check_jwt_token(jwt_token)
        print(validate_jwt_token)
        if validate_jwt_token == 100:
            user_details = get_user_data_by_jwt(jwt_token)
            file_name, system_file_path, global_url, background_url = get_file_path_from_url(body)
            bg_remove_and_blur = self_background_blur_fun(file_name, system_file_path)
            insert_or_update_user_image(file_name = file_name, email = user_details["email"], url = global_url)
            response = Response()
            response.message = constants.SUCCESSFULLY_PERFORMED
            response.url = global_url
            return JSONResponse(status_code=status.HTTP_200_OK, content=response.dict(exclude_none=True))
    except Exception as e:
        print(e)
        response = Response()
        response.message = constants.ERROR
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.dict(exclude_none=True))

@router.post("/background_remove_and_blur")
async def background_remove_and_blur(request: Request) -> JSONResponse:
    try:
        body = await request.json()
        jwt_token = get_jwt_token(request)
        validate_jwt_token = check_jwt_token(jwt_token)
        print(validate_jwt_token)
        if validate_jwt_token == 100:
            user_details = get_user_data_by_jwt(jwt_token)
            file_name, system_file_path, global_url, background_path = get_file_path_from_url(body)
            bg_remove_and_blur = background_remove_and_blur_fun(file_name, system_file_path, background_path)
            insert_or_update_user_image(file_name = file_name, email = user_details["email"], url = global_url)
            response = Response()
            response.message = constants.SUCCESSFULLY_PERFORMED
            response.url = global_url
            return JSONResponse(status_code=status.HTTP_200_OK, content=response.dict(exclude_none=True))
    except Exception as e:
        print(e)
        response = Response()
        response.message = constants.ERROR
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response.dict(exclude_none=True))