from enum import Enum
from typing import List

from pydantic import BaseModel


class FuelType(str, Enum):
    gasoline = "бензин"
    diesel = "дизель"
    electric = "электричество"
    hybrid = "гибрид"

class TransmissionType(str, Enum):
    manual = "механическая"
    automatic = "автоматическая"
    cvt = "вариатор"
    robot = "робот"

class CarBase(BaseModel):
    brand: str
    model: str
    year: int
    fuel_type: FuelType
    transmission_type: TransmissionType
    mileage: float
    price: float

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int

    class Config:
        from_attributes = True

class CarListResponse(BaseModel):
    cars: List[Car]