from pydantic import BaseModel

class Label(BaseModel):
    id: int = None
    name: str
