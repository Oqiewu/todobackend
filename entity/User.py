from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    id: int = None
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = True

class LoginUser(BaseModel):
    email: EmailStr
    hashed_password: str