from fastapi import APIRouter, HTTPException
from general.models import EndpointCreateRequest
from typing import Dict

router = APIRouter(prefix="/general", tags=["General"])

# Dictionary to store dynamically created endpoints
dynamic_endpoints: Dict[str, str] = {}

def create_dynamic_endpoint(path: str, response_message: str):
    """
    Function to dynamically create a new endpoint.
    """
    async def dynamic_endpoint():
        return {"message": response_message}

    # Import the main FastAPI app and add the new route
    from main import app
    app.add_api_route(path, dynamic_endpoint, methods=["GET"])

@router.post("/create/")
async def create_endpoint(request: EndpointCreateRequest):
    """
    Endpoint to create a new dynamic endpoint.
    """
    if request.path in dynamic_endpoints:
        raise HTTPException(
            status_code=400,
            detail="This endpoint already exists."
        )

    # Create the new endpoint
    create_dynamic_endpoint(request.path, request.response_message)
    dynamic_endpoints[request.path] = request.response_message

    return {"message": f"Endpoint with path '{request.path}' created successfully."}

@router.get("/list/")
async def list_endpoints():
    """
    Endpoint to list all dynamically created endpoints.
    """
    return {"dynamic_endpoints": dynamic_endpoints}