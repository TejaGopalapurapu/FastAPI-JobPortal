from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------------------
# Replace with your real PostgreSQL credentials:
# ------------------------
DB_HOST = "localhost"
DB_NAME = "NaukriAPI_Dbo"
DB_USER = "postgres"
DB_PASS = "Teja@6301"
DB_PORT = "5432"

# 1️⃣ Create a connection URL string
#SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL = "postgresql://postgres:Teja%406301@localhost:5432/NaukriAPI_Dbo"



# 2️⃣ Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# 3️⃣ Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4️⃣ Create a base class for models to inherit from
Base = declarative_base()
