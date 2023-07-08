from fastapi import FastAPI
from router import user
import uvicorn

app = FastAPI()

app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000,reload=True)