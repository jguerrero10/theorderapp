from typing import Optional

from pydantic import BaseModel, constr, Field, create_model
from sqlalchemy import Column, Integer, String, UniqueConstraint

from db.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    logo = Column(String(255), nullable=True)

    __table_args__ = (UniqueConstraint('name', name='_name_uc'),)


class RestaurantSchema(BaseModel):
    name: constr(strict=True) = Field(...)
    logo: Optional[str] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "The Fake Restaurant",
                "logo": "/route/to/logo.jpg"
            }
        }

    @classmethod
    def as_optional(cls):
        annotations = cls.__fields__
        fields = {
            attribute: (Optional[data_type.type_], None)
            for attribute, data_type in annotations.items()
        }
        optional_model = create_model(f"Optional{cls.__name__}", **fields)
        return optional_model
