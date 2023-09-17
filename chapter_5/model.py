from pydantic import BaseModel, Field #, constr

class Creature(BaseModel):
    name: str = Field(..., min_length=2)
    # or -> name: str = constr(min_length=2)
    description: str
    location: str