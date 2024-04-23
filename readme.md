# main.py

It serves as the entry point of the application, there are 3 endpoints in this project.

# Login 
For login purpose

# Signup
To signup a user, on signup each user is awarded 3 credits so he is able to summarize 3 pdf documents for free

# Summarzie pdf

For summarization user should first sign up and then login using the endpoint for login, then using the frontend user can easily summarize upto three pdf documents.

This endpoint is protected through JWT-Auth, so its only accessible to registered users

# /credits

This enpoint is used to fetch the remaining credits of every user. Through the jwt it identifies a user and then fetch user credits.

# How to run the project

pip install -r requirements.txt

uvicorn main:app --reload