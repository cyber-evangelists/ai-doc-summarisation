from PyPDF2 import PdfReader
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("API_KEY"))


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def send_to_gpt(text,temperature=0.7, max_tokens=150):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are being provided with all the extracted text from a pdf file, Your job is to summarize the text. Remove the AI Tone"},
        {"role": "user", "content": text},
     
    ], temperature=temperature,
        max_tokens=max_tokens
)
    return response
    # return(response.choices[0].message.content)


