from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from models.mixin import TimeStampMixin  
from models.user import User
from models.associateTable import post_tag_association
from models import Base             


class Post(TimeStampMixin, Base):
    __tablename__ = "Posts"

    # Primary key ID
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    is_published = Column(Boolean, nullable=False, default=False)
    user_id = Column(Integer, ForeignKey('Users.id'))

    # Relationship with the User model (assumes User.posts is defined)
    author = relationship("User", back_populates="posts")

    tags = relationship("Tag", secondary=post_tag_association, back_populates="posts")

