from typing import Optional
from sqlmodel import SQLModel, Field

class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    year: int
    genre: str