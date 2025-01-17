# app/main.py
from fastapi import FastAPI
from general.routers import router as general_router
from general.utils import load_existing_endpoints
from config.database import engine, metadata

app = FastAPI()

# Include routers
app.include_router(general_router)

@app.on_event("startup")
async def startup():
    # Create tables in the database (if they don't exist)
    metadata.create_all(bind=engine)

    # Load existing endpoints from the database
    load_existing_endpoints(app)

@app.get("/")
async def root():
    return {"message": "Welcome to Sharky!"}