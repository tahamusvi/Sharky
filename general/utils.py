# app/general/utils.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from config.database import engine, endpoints
from fastapi import FastAPI, APIRouter

def load_existing_endpoints(app: FastAPI):
    """
    Load all existing endpoints from the database and add them to the FastAPI app.
    """
    # Create a session for working with the database
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    # Fetch all endpoints from the database
    result = db.execute(select(endpoints)).fetchall()

    # Create a new router for dynamic endpoints
    dynamic_router = APIRouter()

    # Add each endpoint to the router
    for row in result:
        path = row.path
        method = row.method.lower()  # Convert method to lowercase (e.g., "get", "post")
        response_message = row.response_message

        # Define the endpoint handler with a closure-safe approach
        async def endpoint_handler(response_message=response_message):  # Fix: Use default parameter
            return {"message": response_message}

        # Add the endpoint to the router
        dynamic_router.add_api_route(
            path=path,
            endpoint=endpoint_handler,
            methods=[method],  # Use the method from the database
        )

    # Include the dynamic router in the main app
    app.include_router(dynamic_router)

    db.close()