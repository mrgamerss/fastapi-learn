from fastapi import APIRouter, Depends
from database import get_db
import schemas
from sqlalchemy.orm import Session
from repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/', response_model=schemas.UserResponse)
def create_user(request: schemas.UserCreate,db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.UserResponse)
def get_user(id:int, db:Session = Depends(get_db)):
    return user.get_user(id, db)