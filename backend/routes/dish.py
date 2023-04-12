from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from models.dishModels import DishSchema, Dish

dish_router = APIRouter()


@dish_router.get("/", response_model=list[DishSchema])
async def get_dishes(db: Session = Depends(get_db)):
    dishes = db.query(Dish).all()
    return dishes


@dish_router.get("/{dish_id}", response_model=DishSchema)
async def get_dish(dish_id: int, db: Session = Depends(get_db)):
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return dish


@dish_router.post("/", response_model=DishSchema)
async def create_dish(dish: DishSchema, db: Session = Depends(get_db)):
    db_dish = Dish(**dish.dict())
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


@dish_router.put("/{dish_id}", response_model=DishSchema)
async def update_dish(dish_id: int, dish: DishSchema, db: Session = Depends(get_db)):
    db_dish = db.query(Dish).filter(Dish.id == dish_id).first()
    if not db_dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    db_dish.name = dish.name
    db_dish.price = dish.price
    db.commit()
    db.refresh(db_dish)
    return db_dish


@dish_router.delete("/{dish_id}")
async def delete_dish(dish_id: int, db: Session = Depends(get_db)):
    db_dish = db.query(Dish).filter(Dish.id == dish_id).first()
    if not db_dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    db.delete(db_dish)
    db.commit()
    return {"message": "Dish deleted"}
