from datetime import datetime
from pydantic import field_validator
from sqlmodel import SQLModel, Field

class BaseEntity(SQLModel, table=False):
    create_time: datetime
    create_id: int
    update_time: datetime
    update_id: int
    version: int = Field(default=1, nullable=False)
    remark: str
    is_deleted: bool = Field(default=False)
    
    @field_validator('is_deleted', mode='before')
    @classmethod
    def convert_int_to_bool(cls, v):
        if isinstance(v, int):
            return bool(v)
        return v
    
    __mapper_args__ = {
        "version_id_col": "version"
    }