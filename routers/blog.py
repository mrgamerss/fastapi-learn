from fastapi import APIRouter, Depends, status
import schemas
from database import get_db
from typing import List
from sqlalchemy.orm import Session
from repository import blog
from oath2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/', response_model=List[schemas.BlogResponse])
def all(db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogCreate, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(get_current_user)):
    return blog.destroy(id, db)
    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.BlogResponse,db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(get_current_user)):
    return blog.update(id, request, db)

@router.get('/{id}', response_model=schemas.BlogResponse, )
def show(id: int, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(get_current_user)):
    return blog.show(id, db)
