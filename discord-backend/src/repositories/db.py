from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from src.config import CONFIG


engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI, encoding="utf-8", echo=True)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()

class USER(Base):
    __tablename__ = 'USER'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=True)
    email = Column(String(256), nullable=True)
    password = Column(String(256), nullable=True)

Base.metadata.create_all(bind=engine)
