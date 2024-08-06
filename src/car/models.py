import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import enum
from sqlalchemy import Integer, String, Enum, Float
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class FuelType(str, enum.Enum):
    gasoline = "бензин"
    diesel = "дизель"
    electric = "электричество"
    hybrid = "гибрид"

class TransmissionType(str, enum.Enum):
    manual = "механическая"
    automatic = "автоматическая"
    cvt = "вариатор"
    robot = "робот"

class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String, index=True, nullable=False)
    model: Mapped[str] = mapped_column(String, index=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    fuel_type: Mapped[FuelType] = mapped_column(Enum(FuelType), index=True, nullable=False)
    transmission_type: Mapped[TransmissionType] = mapped_column(Enum(TransmissionType), index=True, nullable=False)
    mileage: Mapped[float] = mapped_column(Float, index=True, nullable=False)
    price: Mapped[float] = mapped_column(Float, index=True, nullable=False)