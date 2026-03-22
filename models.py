from sqlalchemy import Column, String, Float, Date, ForeignKey
from database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String, primary_key=True, index=True)
    supplier_name = Column(String, index=True)
    vehicle_model = Column(String)
    daily_rate_eur = Column(Float)
    emissions_co2_kg = Column(Float)
    availability_status = Column(String, default="Available", index=True)

class Booking(Base):
    __tablename__ = "bookings"

    booking_reference = Column(String, primary_key=True, index=True)
    vehicle_id = Column(String, ForeignKey("vehicles.id"))
    partner_id = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    total_price = Column(Float)
    status = Column(String, default="Confirmed")


from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class BookingRequest(BaseModel):
    # Enforcing strict types and adding metadata for the Swagger UI docs
    partner_id: str = Field(..., description="The canonical ID of the B2B partner (e.g., 'EASYJET')")
    supplier_id: str = Field(..., description="The ID of the local rental supplier")
    pickup_location: str = Field(..., min_length=3, max_length=3,
                                 description="Standard 3-letter IATA airport code (e.g., 'CDG')")
    pickup_time: datetime = Field(..., description="ISO 8601 formatted datetime for pickup")
    customer_age: int = Field(..., ge=18, le=99, description="Customer age must be 18 or older")

    # Example of a nullable/optional field
    flight_number: Optional[str] = Field(None, description="Optional flight number for delayed arrival tracking")