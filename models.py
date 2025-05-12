from sqlalchemy import Column, Integer, String
from app.database import Base

# 1️⃣ Define the User table (Class)
class User(Base):
    __tablename__ = "users"  # Name of the table in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    name = Column(String, index=True)  # Name column, can be indexed for faster search
    email = Column(String, unique=True, index=True)  # Email column, unique constraint
    password = Column(String)  # Password column, plain text for now (secure later)

# 2️⃣ Define the Job table (Class)
class Job(Base):
    __tablename__ = "jobs"  # Name of the table in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    title = Column(String, index=True)  # Job title column
    description = Column(String)  # Job description column
    company = Column(String)  # Company offering the job
    location = Column(String)  # Location of the job
