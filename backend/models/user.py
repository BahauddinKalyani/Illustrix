from mongoengine import Document, StringField, DateTimeField,
from datetime import datetime

class User(Document):
    first_name = StringField(max_length=100)
    last_name = StringField(max_length=100)
    email = StringField(required=True, max_length=100)
    password = StringField(max_length=100)
    created_at: DateTimeField(default=datetime.utcnow())
    updated_at: DateTimeField(default=datetime.utcnow())