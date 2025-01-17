# app/general/routers.py
from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import sessionmaker
from .models import EndpointCreateRequest, EndpointResponse,EndpointDeleteRequest
from config.database import engine, endpoints
from fastapi import FastAPI

router = APIRouter(prefix="/general", tags=["General"])

# Create a session for working with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to dynamically create and register an endpoint
def create_dynamic_endpoint(path: str, method: str, response_message: str):
    """
    Dynamically creates and registers a new endpoint with FastAPI.
    """
    async def dynamic_endpoint():
        return {"message": response_message}

    # Import the FastAPI app instance
    from main import app

    # Register the new endpoint with FastAPI
    app.add_api_route(
        path=path,
        endpoint=dynamic_endpoint,
        methods=[method.upper()],  # Ensure the method is uppercase (e.g., GET, POST)
    )

@router.post("/create/")
async def create_endpoint(request: EndpointCreateRequest):
    db = SessionLocal()
    # Check if an endpoint with the same path already exists
    existing_endpoint = db.execute(
        select(endpoints).where(endpoints.c.path == request.path)
    ).fetchone()
    if existing_endpoint:
        raise HTTPException(status_code=400, detail="This endpoint already exists.")

    # Insert the new endpoint into the database
    db.execute(
        insert(endpoints).values(
            path=request.path,
            method=request.method,
            response_message=request.response_message,
            schema=request.schema,
        )
    )
    db.commit()

    # Dynamically register the new endpoint with FastAPI
    create_dynamic_endpoint(request.path, request.method, request.response_message)

    return {"message": f"Endpoint with path '{request.path}' created successfully."}

@router.get("/list/", response_model=list[EndpointResponse])
async def list_endpoints():
    db = SessionLocal()
    # Fetch all endpoints from the database
    result = db.execute(select(endpoints)).fetchall()
    
    # Convert SQLAlchemy Row objects to Pydantic models
    endpoints_list = [
        EndpointResponse(
            id=row.id,
            path=row.path,
            method=row.method,
            response_message=row.response_message,
            schema=row.schema,
        )
        for row in result
    ]
    
    return endpoints_list

@router.delete("/delete/")
async def delete_endpoint(request: EndpointDeleteRequest):
    db = SessionLocal()
    # Delete the endpoint from the database
    db.execute(delete(endpoints).where(endpoints.c.path == request.path))
    db.commit()
    return {"message": f"Endpoint with path '{request.path}' deleted successfully."}

@router.put("/update/")
async def update_endpoint(request: EndpointCreateRequest):
    db = SessionLocal()
    # Update the endpoint in the database
    db.execute(
        update(endpoints)
        .where(endpoints.c.path == request.path)
        .values(
            method=request.method,
            response_message=request.response_message,
            schema=request.schema,
        )
    )
    db.commit()

    create_dynamic_endpoint(request.path, request.method, request.response_message)

    return {"message": f"Endpoint with path '{request.path}' updated successfully."}