from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db.database import get_db
from helpers.restaurant import restaurant_helper
from models.RestaurantModel import RestaurantSchema, Restaurant

restaurant_router = APIRouter()


@restaurant_router.post("/")
async def create_restaurant(restaurant: RestaurantSchema, db: Session = Depends(get_db)):
    try:
        db_restaurant = Restaurant(name=restaurant.name, logo=restaurant.logo)
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        return restaurant_helper(db_restaurant)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Duplicate value for unique column")


@restaurant_router.get("/")
async def get_restaurants(db: Session = Depends(get_db)):
    restaurants = db.query(Restaurant).all()
    return [restaurant_helper(restaurant) for restaurant in restaurants]


@restaurant_router.get("/{restaurant_id}")
async def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail=f"The restaurant with id {restaurant_id} is not found")
    return restaurant_helper(restaurant)


@restaurant_router.put("/{restaurant_id}")
async def update_restaurant(restaurant_id: int, restaurant: RestaurantSchema, db: Session = Depends(get_db)):
    try:
        db_restaurant = db.query(Restaurant).get(restaurant_id)
        if not db_restaurant:
            raise HTTPException(status_code=404, detail=f"The restaurant with id {restaurant_id} is not found")
        db_restaurant.name = restaurant.name
        db_restaurant.logo = restaurant.logo
        db.commit()
        db.refresh(db_restaurant)
        return restaurant_helper(db_restaurant)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Duplicate value for unique column")


@restaurant_router.delete("/{restaurant_id}")
async def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = db.query(Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail=f"The restaurant with id {restaurant_id} is not found")
    db.delete(db_restaurant)
    db.commit()
    return {"message": "Restaurant deleted"}
