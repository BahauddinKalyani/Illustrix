from mongoengine import Document, StringField, DateTimeField,
from datetime import datetime

class Image(Document):
    user_id = StringField(required=True)
    filename = StringField(required=True)
    url = StringField(required=True)
    created_at: DateTimeField(default=datetime.utcnow())
    updated_at: DateTimeField(default=datetime.utcnow())        
