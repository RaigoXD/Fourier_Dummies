from pydantic import BaseModel, Field


class Function(BaseModel):
    function: str = Field(max_length=45)
    upper_limit:str = Field(max_length=10)
    lower_limit:str = Field(max_length=40)