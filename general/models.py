# app/general/models.py
from pydantic import BaseModel
from typing import Optional, Dict

class EndpointCreateRequest(BaseModel):
    path: str
    method: str  # e.g., GET, POST, PUT, DELETE
    response_message: str
    schema: Optional[Dict] = None  # For custom data structures

class EndpointResponse(BaseModel):
    id: int
    path: str
    method: str
    response_message: str
    schema: Optional[Dict] = None

class EndpointDeleteRequest(BaseModel):
    path: str