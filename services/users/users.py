from fastapi import APIRouter, HTTPException
from typing import List
from flask import jsonify
from pydantic import BaseModel
from sqlalchemy import create_engine
from users.user_model import User, UserResponse,UserRequest
from users.user_controller import user_controller
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


router = APIRouter()
    
@router.get("/getAllUsers", response_model=List[UserResponse])
def getAllUsers():
    users = user_controller.getAllUsers()
    return users

@router.post("/addUser", response_model=UserResponse)
def getAllUsers(user: UserRequest):
    user = user_controller.addUser(user.dict())
    return user

@router.post("/login", response_model=bool)
def login(user: UserRequest):
    print(user.email)
    status = user_controller.login(email=user.email,password=user.password)
    return status

@router.get("/getdata", response_model=str)
@login_required
def getdata():
    # Bu servise sadece login olan kullanıcılar erişebilir
    return "test"

@router.get("/getUser/{user_id}", response_model=UserResponse)
def getUserById(user_id: int):
    user = user_controller.getUserById(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/deleteUser/{user_id}")
def deleteUserById(user_id: int):
    success = user_controller.deleteUserById(user_id)
    if success:
        return success
    else:
        raise HTTPException(status_code=404, detail="User not found")