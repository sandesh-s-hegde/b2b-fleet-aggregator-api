from sqlalchemy import Column, String, Float
from database import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(String, primary_key=True, index=True)
    role = Column(String, index=True)
    status = Column(String, default="Available")
    fatigue_score = Column(Float, default=0.0)

class AGV(Base):
    __tablename__ = "agvs"

    id = Column(String, primary_key=True, index=True)
    agv_type = Column(String)
    status = Column(String, default="Charging")
    battery_pct = Column(Float, default=100.0)