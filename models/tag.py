from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base,relationship
from models.mixin import TimeStampMixin
from models.associateTable import post_tag_association
from models import Base

class Tag(TimeStampMixin, Base):
    __tablename__ = "Tags"


    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    posts = relationship("Post", secondary=post_tag_association, back_populates="tags")

    # Optional: represent object as a string (useful for admin/debugging)
    def __repr__(self):
        return f"<Tag(name='{self.name}')>"
