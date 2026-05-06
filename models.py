from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Column, Date, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String, primary_key=True, index=True)
    supplier_name = Column(String, index=True)
    vehicle_model = Column(String)
    daily_rate_eur = Column(Float)
    emissions_co2_kg = Column(Float)
    availability_status = Column(String, default="Available", index=True)

    bookings = relationship("Booking", back_populates="vehicle")


class Booking(Base):
    __tablename__ = "bookings"

    booking_reference = Column(String, primary_key=True, index=True)
    vehicle_id = Column(String, ForeignKey("vehicles.id"))
    partner_id = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    total_price = Column(Float)
    status = Column(String, default="Confirmed")

    vehicle = relationship("Vehicle", back_populates="bookings")


class BookingRequest(BaseModel):
    partner_id: str = Field(..., description="Canonical ID of the requesting B2B partner.")
    supplier_id: str = Field(..., description="ID of the fulfillment supplier.")
    pickup_location: str = Field(..., min_length=3, max_length=3, description="3-letter IATA location code.")
    pickup_time: datetime = Field(..., description="Scheduled pickup timestamp.")
    customer_age: int = Field(..., ge=18, le=99, description="Age of the primary driver.")
    flight_number: Optional[str] = Field(default=None, description="Inbound flight identifier for delay tracking.")