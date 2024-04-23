from fastapi import APIRouter, Body
from app.model import UserSchema, UserLoginSchema
from app.db_auth import create_user_in_db, get_user_from_db, check_password
from auth.auth_handler import signJWT

user_router = APIRouter()

@user_router.post("/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    create_user_in_db(user.dict())
    return signJWT(user.email)

@user_router.post("/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
   user_data = get_user_from_db(user.email)
   return check_password(user, user_data)
