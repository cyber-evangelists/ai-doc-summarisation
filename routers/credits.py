from fastapi import APIRouter, UploadFile, File, Depends
from typing import List
from auth.auth_bearer import JWTBearer
from pathlib import Path
from app.credits import get_credits
from app.getUser import get_current_user
credits = APIRouter()

@credits.post("/credits", dependencies=[Depends(JWTBearer())], tags=["Summarize PDFs"])
async def upload_pdf(mail: str = Depends(get_current_user)):
    return(get_credits(mail));
    
    