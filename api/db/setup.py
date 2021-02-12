"""Setup for SQLAlchemy connection to database and other commonly-used functions."""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.db import DATABASE_URL

Base = declarative_base()


def retrieve_database_connection():
    """
    Retrieves the database connection.

    Returns:
        The database connection.
    """
    database_connection = LocalSession()

    try:
        yield database_connection
    except:  # pylint: disable=bare-except
        database_connection.rollback()
    finally:
        database_connection.close()


def create_session(database_url: str):
    """
    Creates a session given a database URL connection.

    Parameters:
        database_url: The database URl to use as the location.

    Returns:
        A tuple containing the local session class
        for instantiating a connection to the database and associated its engine.
    """
    connect_args = {"check_same_thread": False} if os.environ.get("IS_UNIT_TEST") else {}
    engine = create_engine(
        database_url, connect_args=connect_args
    )  # pylint: disable=redefined-outer-name
    LocalSession = sessionmaker(  # pylint: disable=redefined-outer-name
        autocommit=False, autoflush=False, bind=engine
    )

    return LocalSession, engine


LocalSession, engine = create_session(
    DATABASE_URL
)  # pylint: disable=redefined-outer-name,bad-option-value
