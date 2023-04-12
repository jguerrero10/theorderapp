from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from helpers.order import order_helper, orders_active
from models.OrderModels import OrderSchema, Order, OrderDish, OrderStatus

order_router = APIRouter()


@order_router.post("/")
async def create_order(order: OrderSchema, db: Session = Depends(get_db)):
    db_order = Order(
        status=order.status,
        observations=order.observations,
        customer_name=order.customer_name,
        on_site=order.on_site
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    dishes = list()
    for order_dish in order.order_dishes:
        db_order_dish = OrderDish(
            order_id=db_order.id,
            dish_id=order_dish.dish_id,
            quantity=order_dish.quantity
        )
        db.add(db_order_dish)
        db.commit()
        db.refresh(db_order_dish)
        dishes.append(db_order_dish)
    return order_helper(db_order)


@order_router.put("/{order_id}")
async def update_status_order(order_id: int, status: OrderStatus, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.status = status
    if status == OrderStatus.DELIVERED:
        db_order.is_active = False
    db.commit()
    return order_helper(db_order)


@order_router.get("/")
async def get_active_order(db: Session = Depends(get_db)):
    orders = list()
    for order in db.query(Order).filter(Order.is_active == True):
        orders.append(orders_active(order))
    return orders


@order_router.get("/{order_id}")
async def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_helper(order)
