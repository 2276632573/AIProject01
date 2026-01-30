from datetime import datetime
from typing import Optional
from pydantic import field_validator
from sqlmodel import SQLModel, Field, Session, column

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
    
    def increment_version(self):
        if self.version is None:
            self.version = 1
        else:
            self.version += 1

    @classmethod
    def update_with_version(
        cls,
        session: Session,
        obj_id: int,
        update_data: dict,
        expected_version: int
    ):
        obj = session.get(cls, obj_id)
        if obj is None:
            raise ValueError("Object not found")
        if obj.version != expected_version:
            raise ValueError("Version conflict detected")
        
        for key, value in update_data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        
        obj.increment_version()
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj