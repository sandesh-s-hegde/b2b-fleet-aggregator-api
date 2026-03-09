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