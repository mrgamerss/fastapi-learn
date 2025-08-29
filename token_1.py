from datetime import datetime, timedelta
from jose import JWTError, jwt, ExpiredSignatureError
from typing import Optional
import schemas
from fastapi import HTTPException, status

SECRETE_KEY = "SECRETE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRETE_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRETE_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
        return token_data
    
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired. Please log in again."
        )
    
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token validation error: {str(e)}"
        )