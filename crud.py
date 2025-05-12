from sqlalchemy.orm import Session
from app import models, schemas
from app.models import User, Job

# 1️⃣ Create a user (Handle user creation in DB)
def create_user(db: Session, user: schemas.UserCreate):
    # Create a new User object
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)  # Add the user to the session
    db.commit()  # Commit the session to save the user in DB
    db.refresh(db_user)  # Refresh to get the latest state (like the id after insertion)
    return db_user

# 2️⃣ Get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# 3️⃣ Get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# 4️⃣ Create a job (Handle job creation in DB)
def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(title=job.title, description=job.description, company=job.company, location=job.location)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

# 5️⃣ Get all jobs
def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()

# 6️⃣ Get a job by ID
def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()
