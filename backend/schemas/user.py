from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime