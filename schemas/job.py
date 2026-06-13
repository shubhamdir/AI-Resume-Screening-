from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    domain: str
    description: str