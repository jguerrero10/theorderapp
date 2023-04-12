from fastapi import FastAPI

from db.database import Base, engine
from routes.dish import dish_router
from routes.order import order_router
from routes.restaurant import restaurant_router

app = FastAPI()
app.include_router(restaurant_router, tags=["Restaurants"], prefix="/restaurant")
app.include_router(dish_router, tags=["Dish"], prefix="/dish")
app.include_router(order_router, tags=["Order"], prefix="/order")

Base.metadata.create_all(bind=engine)


@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Welcome to The Order App"}
