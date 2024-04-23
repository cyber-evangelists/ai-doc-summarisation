# Main.py

It serves as the entry point of the application, there are 4 endpoints in this project.
1) /login
2) /signup
3) /credits
4) /summarize

User data has been saved in Mongodb

# Login 
For login purpose

# Signup
To signup a user, on signup each user is awarded 3 credits so he is able to summarize 3 pdf documents for free

# Summarzie pdf

For pdf summarization we have used chatgpt-3.5-turbo model. It reads document thoroughly and then outputs a brief but concise summary.

For summarization user should first sign up and then login using the endpoint for login, then using the frontend user can easily summarize upto three pdf documents.

This endpoint is protected through JWT-Auth, so its only accessible to registered users


# How does credits work

This enpoint is used to fetch the remaining credits of every user. Through the jwt it identifies a user and then fetch user credits. Each user is awarded 3 credits so he is able to summarize 3 pdf documents for free


## Environment Variables

Create a .env file in the root and  follow .env.example to add all the environmental variables in it.

`API_KEY`

`ANOTHER_API_KEY`



## Deployment
-> You should have Mongodb Server installed in the system

To deploy this project run

```bash
  pip install -r requirements.txt
  uvicorn main:app --reload

```



