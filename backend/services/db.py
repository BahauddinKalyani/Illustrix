from mongoengine import connect
from ..config import db_settings

def connect_mongo_db():
    connect(db=db_settings.db_name, host=db_settings.db_host, port=db_settings.db_port)