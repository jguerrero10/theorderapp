from fastapi import FastAPI

from db.database import Base, engine
from routes.restaurant import restaurant_router

app = FastAPI()
app.include_router(restaurant_router, tags=["Restaurants"], prefix="/restaurant")

Base.metadata.create_all(bind=engine)


@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Welcome to The Order App"}
