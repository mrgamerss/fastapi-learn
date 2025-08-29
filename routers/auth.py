from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import database
from sqlalchemy.orm import Session
import models
from hashing import Hash
from datetime import timedelta
from token_1 import  create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login",
    tags=['Auth']
)

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid creditial')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')
    
    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}