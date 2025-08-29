from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship


class Blog(Base):
    __tablename__ = 'blogs'

    id:Mapped[int] = Column(Integer, primary_key=True, index=True)
    title:Mapped[str] = Column(String)
    body:Mapped[str] = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")