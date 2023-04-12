from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, DateTime, ForeignKey, func, Boolean, String
from sqlalchemy.orm import relationship

from db.database import Base


class OrderStatus(str, Enum):
    REQUESTED = "requested"
    PREPARING = "preparing"
    READY = "ready"
    DELIVERED = "delivered"


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String(50), nullable=False)
    customer_name = Column(String(80), nullable=False)
    is_active = Column(Boolean, default=True)
    observations = Column(String(255), nullable=True)
    on_site = Column(Boolean, nullable=False)

    order_items = relationship("OrderDish", back_populates="order")

    def __int__(self, order_status: OrderStatus, **data):
        super().__init__(**data)
        self.status = order_status.value


class OrderDish(Base):
    __tablename__ = "order_dishes"

    id = Column(Integer, primary_key=True, index=True)
    dish_id = Column(Integer, ForeignKey("dishes.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    quantity = Column(Integer)

    dish = relationship("Dish", back_populates="orders")
    order = relationship("Order", back_populates="order_items")


class OrderDishSchema(BaseModel):
    dish_id: int
    quantity: int

    class Config:
        orm_mode = True


class OrderSchema(BaseModel):
    order_date: Optional[datetime] = datetime.now()
    total: float = 0
    status: Optional[OrderStatus]
    observations: Optional[str] = None
    on_site: bool
    customer_name: str
    order_dishes: List[OrderDishSchema]

    class Config:
        orm_mode = True
