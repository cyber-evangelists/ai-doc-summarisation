from fastapi import Header, HTTPException
from auth.auth_handler import decodeJWT

async def get_current_user(authorization: str = Header(...)):
    try:
        token = authorization.split()[1] 
        payload = decodeJWT(token) 
        if payload:
            user_id = payload.get("user_id") 
            return user_id
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
    except IndexError:
        raise HTTPException(status_code=401, detail="Token missing or invalid format")
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
