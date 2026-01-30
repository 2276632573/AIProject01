from sqlmodel import Field
from .BaseEntity import BaseEntity

class User(BaseEntity, table=True):
    __tablename__ = "py_user"
    id: int = Field(default=None, primary_key=True)
    name: str
    type: str