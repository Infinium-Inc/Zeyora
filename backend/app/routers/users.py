from ..database import getDB
from .. import schemas
from .. import models
from .. import utils

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post("/", response_model=schemas.UserResponse, status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(getDB)):    
    validation = utils.validate_password(user.password)
    if validation != True:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail=validation
        )

    user.password = utils.hash(user.password)  
    db_user = models.User(**user.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user