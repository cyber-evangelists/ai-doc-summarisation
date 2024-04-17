from fastapi import APIRouter, UploadFile, File, Depends
from typing import List
from auth.auth_bearer import JWTBearer
from app.chatgpt import extract_text_from_pdf, send_to_gpt
from app.credits import check_credits, update_credits

pdf_router = APIRouter()

@pdf_router.post("/summarize", dependencies=[Depends(JWTBearer())], tags=["Summarize PDFs"])
async def upload_pdf(files: List[UploadFile] = File(...)):
    if(check_credits()==True):
        for uploaded_file in files:
            contents = await uploaded_file.read()
            with open(uploaded_file.filename, "wb") as f:
                f.write(contents)
            text = extract_text_from_pdf(uploaded_file.filename)
            if(update_credits()==True):
                return send_to_gpt(text)
            else:
                return("You dont have enough credits")          
    else:
        return("You dont have enough credits")
