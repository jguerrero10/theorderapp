from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import Base, engine
from routes.dish import dish_router
from routes.order import order_router
from routes.restaurant import restaurant_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(restaurant_router, tags=["Restaurants"], prefix="/restaurant")
app.include_router(dish_router, tags=["Dish"], prefix="/dish")
app.include_router(order_router, tags=["Order"], prefix="/order")

Base.metadata.create_all(bind=engine)


@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Welcome to The Order App"}
