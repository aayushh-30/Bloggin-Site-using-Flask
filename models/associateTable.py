from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

# This is a bridge table with two foreign keys
post_tag_association = Table(
    "post_tag_association", Base.metadata,
    Column("post_id", Integer, ForeignKey("Posts.id")),
    Column("tag_id", Integer, ForeignKey("Tags.id"))
)
