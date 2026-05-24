from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:aditya123@localhost:5432/Notes_APP"
## db_url_format = postgresql://username:password@host:port/database

engine = create_engine(db_url)

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

# this file allows my app to talk to my database
