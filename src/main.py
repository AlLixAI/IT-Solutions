from fastapi import FastAPI
from src.car.router import router as router_car

app = FastAPI()

app.include_router(router_car)
