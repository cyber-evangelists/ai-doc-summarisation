from decouple import config
from openai import OpenAI
API= config("API_KEY")

client=OpenAI(api_key=API)


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Can you summarize the main points of this article on renewable energy?"},
    {"role": "assistant", "content": ""},
  ]
)
