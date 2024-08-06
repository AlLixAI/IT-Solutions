from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.car.schemas import CarCreate, CarListResponse
from src.database import get_async_session
from src.car import models, schemas

router = APIRouter(
    prefix="/cars",
    tags=["Cars"],
)

@router.post("/", response_model=schemas.Car)
async def add_car(
    session: AsyncSession = Depends(get_async_session),
    car: CarCreate = Depends(CarCreate)
):
    try:
        car_data = car.dict()
        car_data['brand'] = car_data['brand'].lower()
        car_data['model'] = car_data['model'].lower()

        if car_data['price'] < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Price must be > than 0")
        if car_data['mileage'] < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mileage must be >= than 0")
        if car_data['year'] < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Year must be >= than 0")

        new_car = models.Car(**car_data)
        session.add(new_car)

        await session.commit()

        return new_car

    except HTTPException as http_exc:
        await session.rollback()
        raise http_exc

    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/", response_model=schemas.CarListResponse)
async def get_cars(
    session: AsyncSession = Depends(get_async_session),
    brand: Optional[str] = None,
    model: Optional[str] = None,
    year: Optional[int] = None,
    fuel_type: Optional[schemas.FuelType] = None,
    transmission_type: Optional[schemas.TransmissionType] = None,
    min_mileage: Optional[float] = None,
    max_mileage: Optional[float] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    limit: int = Query(10, le=100),
    offset: int = Query(0, ge=0)
):
    try:
        query = select(models.Car)
        if brand:
            query = query.where(models.Car.brand == brand.lower())
        if model:
            query = query.where(models.Car.model == model.lower())
        if year:
            query = query.where(models.Car.year == year)
        if fuel_type:
            query = query.where(models.Car.fuel_type == fuel_type)
        if transmission_type:
            query = query.where(models.Car.transmission_type == transmission_type)
        if min_mileage is not None:
            query = query.where(models.Car.mileage >= min_mileage)
        if max_mileage is not None:
            query = query.where(models.Car.mileage <= max_mileage)
        if min_price is not None:
            query = query.where(models.Car.price >= min_price)
        if max_price is not None:
            query = query.where(models.Car.price <= max_price)

        query = query.limit(limit).offset(offset)

        result = await session.execute(query)
        cars = result.scalars().all()

        return schemas.CarListResponse(cars=cars)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/{car_id}", response_model=schemas.Car)
async def get_car_by_id(
    car_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    query = select(models.Car).where(models.Car.id == car_id)
    result = await session.execute(query)
    car = result.scalars().first()

    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return car