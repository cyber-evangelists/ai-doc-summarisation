from pymongo import MongoClient
import os
mongo_client = MongoClient(os.environ.get('URI'))
db = mongo_client['openAI_PDF']
users_collection = db["users"]
def check_credits(mail):
    user = users_collection.find_one({"email": mail})  
    if user:
        current_credits = user.get("credits", 0) 
        if current_credits > 0:
            return True
        else:
            return False
    else:
        return False
def update_credit(mail):
    user = users_collection.find_one({"email": mail})  
    if user:
        current_credits = user.get("credits", 0) 
        if current_credits > 0:
            new_credits = current_credits - 1
            users_collection.update_one({"email": mail}, {"$set": {"credits": new_credits}})
        else:
           return("You dont have enough credits")
    else:
        return False

def get_credits(mail):
    user = users_collection.find_one({"email": mail})  
    if user:
        current_credits = user.get("credits", 0) 
        return current_credits
    
