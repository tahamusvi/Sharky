# app/database.py
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, JSON

# SQLite database settings
DATABASE_URL = "sqlite:///./sharky.db"

# Create database engine
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define table for storing endpoints
endpoints = Table(
    "endpoints",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("path", String, unique=True, index=True),
    Column("method", String),  # e.g., GET, POST, PUT, DELETE
    Column("response_message", String),
    Column("schema", JSON, nullable=True),  # For custom data structures
)

# Create tables in the database
metadata.create_all(bind=engine)