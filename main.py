from fastapi import FastAPI
from routers.user import user_router
from routers.pdf import pdf_router

app = FastAPI()

app.include_router(user_router)
app.include_router(pdf_router)
