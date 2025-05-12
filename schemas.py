from pydantic import BaseModel
from typing import List, Optional

# 1️⃣ User Schema (For Requests & Responses)
class UserBase(BaseModel):
    name: str
    email: str

# Schema for user creation (Request - takes in password)
class UserCreate(UserBase):
    password: str

# Schema for user response (doesn't include password)
class UserResponse(UserBase):
    id: int  # Will be populated after user is created
    class Config:
        orm_mode = True  # Tells Pydantic to treat this like an ORM model

# 2️⃣ Job Schema (For Requests & Responses)
class JobBase(BaseModel):
    title: str
    description: str
    company: str
    location: str

# Schema for job creation (Request)
class JobCreate(JobBase):
    pass

# Schema for job response (Response)
class JobResponse(JobBase):
    id: int  # Will be populated after job is created
    class Config:
        orm_mode = True  # Tells Pydantic to treat this like an ORM model
