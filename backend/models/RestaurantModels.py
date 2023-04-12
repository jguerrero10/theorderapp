from typing import Optional, List

from pydantic import BaseModel, constr, Field
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from db.database import Base
from models.dishModels import DishSchema


class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    logo = Column(String(255), nullable=True)
    dishes = relationship("Dish", back_populates="restaurant")

    __table_args__ = (UniqueConstraint('name', name='_name_uc'),)


class RestaurantSchema(BaseModel):
    name: constr(strict=True) = Field(...)
    logo: Optional[str] = None
    dishes: List[DishSchema] = []

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "The Fake Restaurant",
                "logo": "/route/to/logo.jpg"
            }
        }
