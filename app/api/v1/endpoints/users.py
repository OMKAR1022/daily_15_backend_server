from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.services.user_service import sign_up, sign_in, get_user, sign_out
from app.schemas.user import UserCreate, Token
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register", response_model=Dict[str, Any])
async def register(user_data: UserCreate):
    return await sign_up(user_data)

@router.post("/login", response_model=Token)
async def login(login_data: LoginRequest):
    response = await sign_in(login_data.email, login_data.password)
    return {
        "access_token": response.session.access_token,
        "token_type": "bearer"
    }

@router.get("/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    user = await get_user(token)
    return user

@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    return await sign_out(token)
