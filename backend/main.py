from fastapi import FastAPI
from router import user, image
import uvicorn

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html = True), name="static")

app.include_router(user.router, prefix="/user")

app.include_router(image.router, prefix="/image")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000,reload=True)
