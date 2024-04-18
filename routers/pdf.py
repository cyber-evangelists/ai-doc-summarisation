from fastapi import APIRouter, UploadFile, File, Depends
from typing import List
from auth.auth_bearer import JWTBearer
from app.chatgpt import extract_text_from_pdf, send_to_gpt
from app.credits import check_credits,update_credit
from app.getUser import get_current_user
from pathlib import Path
import shutil

pdf_router = APIRouter()

@pdf_router.post("/summarize", dependencies=[Depends(JWTBearer())], tags=["Summarize PDFs"])
async def upload_pdf(files: List[UploadFile] = File(...), mail: str = Depends(get_current_user)):

    if check_credits(mail):
        upload_dir = Path("temp")
        upload_dir.mkdir(parents=True, exist_ok=True)
        try: 
            for uploaded_file in files:
                update_credit(mail)
                file_path = upload_dir / uploaded_file.filename
                with open(file_path, "wb") as f:
                    contents = await uploaded_file.read()
                    f.write(contents)
            processed_texts = []
            for uploaded_file in files:
                text = extract_text_from_pdf(str(upload_dir / uploaded_file.filename))
                processed_texts.append(text)
            shutil.rmtree(upload_dir, ignore_errors=True)
            return [send_to_gpt(text) for text in processed_texts]
        except Exception as e:
            shutil.rmtree(upload_dir, ignore_errors=True)
            return {"error": str(e)}
    else:
        return {"error": "You don't have enough credits to process this file"}
