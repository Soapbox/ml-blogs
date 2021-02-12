"""The list of all possible operations for the blogs router."""

from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import or_
from api.db.models import Blogs


def get_blogs(db: Session, categories: Optional[List[str]] = None):
    """
    Retrieves all of the blogs.

    Parameters:
        db: The database session.
        categories: The list of categories to filter on.

    Returns:
        The list of blog posts.
    """
    blogs_query = db.query(Blogs)

    if categories:
        filters = []
        for category in categories:
            filters.append(Blogs.categories.ilike(f"%{category}%"))

        return blogs_query.filter(or_(*filters)).all()

    return blogs_query.all()
