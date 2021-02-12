"""The models used for blogs."""

from sqlalchemy import Column, Integer, Text, String
from api.db import Base


class Blogs(Base):  # pylint: disable=too-few-public-methods
    """The model for the blogs table."""

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    link = Column(Text)
    published_date = Column(String(128))
    image = Column(Text)
    categories = Column(Text)
    author = Column(Text)
