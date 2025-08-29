from typing import List
from pydantic import BaseModel

class Pet(BaseModel):
    animal: str
    sex: str
    descriptors: List[str]