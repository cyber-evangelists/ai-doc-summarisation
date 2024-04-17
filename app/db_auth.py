from PyPDF2 import PdfReader
from openai import OpenAI
from pymongo import MongoClient
import os
import bcrypt
from auth.auth_handler import signJWT

client = OpenAI(api_key=os.environ.get("API_KEY"))
mongo_client = MongoClient(os.environ.get('URI'))
db = mongo_client['openAI_PDF']
users_collection = db["users"]

def create_user_in_db(user_data):
    hashed_password = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt())
    user_data['password'] = hashed_password.decode('utf-8')
    users_collection.insert_one(user_data)

def get_user_from_db(email):
    return users_collection.find_one({"email": email})

def check_password(user,user_data):
    if user_data:
            hashed_password = user_data.get("password")
    if bcrypt.checkpw(user.password.encode('utf-8'), hashed_password.encode('utf-8')):
            return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
    


