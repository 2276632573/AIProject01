from datetime import datetime
from typing import Optional
from pydantic import field_validator
from sqlmodel import SQLModel, Field, column

class BaseEntity(SQLModel, table=False):
    create_time: Optional[datetime] = None
    create_id: Optional[int] = None
    update_time: Optional[datetime] = Field(default_factory=datetime.utcnow)
    update_id: Optional[int] = None
    version: int = Field(default=1, nullable=False)
    remark: Optional[str] = None
    is_deleted: bool = Field(default=False)
    
    @field_validator('is_deleted', mode='before')
    @classmethod
    def convert_int_to_bool(cls, v):
        if isinstance(v, int):
            return bool(v)
        return v
    
    __mapper_args__ = {
        "version_id_col": "version",
        "version_id_generator": False,
    }