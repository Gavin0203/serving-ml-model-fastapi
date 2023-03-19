from pydantic import BaseModel

class ResponseItem(BaseModel):
    prediction : int