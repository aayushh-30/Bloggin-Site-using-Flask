from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.mixin import TimeStampMixin
from models.post import Post
from models import Base

# Simple email validation function
def is_valid_email(email):
    return '@' in email

class User(TimeStampMixin, Base):
    __tablename__ = "Users"


    id = Column(Integer, primary_key=True)
    _email = Column("email", String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)

    # One-to-many relationship: one user can have many posts
    posts = relationship("Post", back_populates="author")

    # Property getter for email
    @property
    def email(self):
        return self._email

    # Property setter with validation
    @email.setter
    def email(self, value):
        if value:
            value = value.strip()
            if not is_valid_email(value):
                raise ValueError(f"Invalid email format: {value}")
            self._email = value
        else:
            raise ValueError("Email cannot be empty")

    # Optional: represent object as a string (useful for debugging)
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
