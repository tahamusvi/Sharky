from pydantic import BaseModel

class EndpointCreateRequest(BaseModel):
    """
    Pydantic model for receiving data to create a new endpoint.
    """
    path: str  # The path of the endpoint (e.g., "/hello")
    response_message: str  # The message the endpoint should return (e.g., "Hello, World!")

class EndpointResponse(BaseModel):
    """
    Pydantic model for defining the response structure of dynamic endpoints.
    """
    message: str  # The response message from the endpoint