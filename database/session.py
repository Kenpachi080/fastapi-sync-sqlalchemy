from core.config import SYNC_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(SYNC_DATABASE_URI, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()