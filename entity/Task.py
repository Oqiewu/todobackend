from pydantic import BaseModel

class Task(BaseModel):
    id: int = None
    text: str
    label_id: int