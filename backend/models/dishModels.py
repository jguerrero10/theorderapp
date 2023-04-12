from typing import Optional

from pydantic import BaseModel, constr, Field
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Dish(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255), nullable=True)
    price = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

    orders = relationship("OrderDish", back_populates="dish")
    restaurant = relationship("Restaurant", back_populates="dishes")


class DishSchema(BaseModel):
    name: constr(strict=True) = Field(...)
    description: Optional[str] = None
    price: int
    restaurant_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Fake Dish",
                "description": "This dish is an exotic combination of flavors "
                               "and textures, where the softness of the avocado, "
                               "the spicy touch of the chili, the freshness of the "
                               "mint and the creaminess of the cheese of the chili, "
                               "the freshness of the mint and the creaminess of the "
                               "goat cheese of goat cheese. All this is accompanied "
                               "by a crunchy bread base toasted bread and a tropical "
                               "fruit sauce that adds a touch of sweetness needed to "
                               "balance the whole. A unique gastronomic experience "
                               "that will not leave you indifferent.",
                "price": 32000,
                "restaurant_id": 1
            }
        }
