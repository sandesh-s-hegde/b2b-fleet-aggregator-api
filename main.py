from datetime import datetime
from typing import List

from fastapi import FastAPI, Response, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

# Initialize database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="B2B Fleet Aggregator API",
    description="CarTrawler-style API connecting logistics platforms to commercial rental suppliers.",
    version="1.0.0"
)


@app.get("/favicon.ico", include_in_schema=False)
async def favicon() -> Response:
    """Silences the browser's default favicon request error."""
    return Response(status_code=204)


@app.get("/", tags=["System"])
async def root() -> dict:
    """Health check endpoint to verify the API is online."""
    return {
        "status": "Online",
        "timestamp": datetime.now(),
        "version": "1.0.0"
    }


@app.post("/api/v1/vehicles", response_model=schemas.VehicleResponse, tags=["Fleet Management"])
async def add_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    """Registers a new commercial vehicle into the supplier database."""
    db_vehicle = models.Vehicle(**vehicle.model_dump())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


@app.get("/api/v1/vehicles", response_model=List[schemas.VehicleResponse], tags=["Fleet Management"])
async def get_all_vehicles(db: Session = Depends(get_db)):
    """Fetches the entire catalog of available supplier vehicles."""
    return db.query(models.Vehicle).all()


@app.post("/api/v1/fleet/search", response_model=List[schemas.VehicleResponse], tags=["Aggregation Engine"])
async def search_fleet_capacity(request: schemas.SearchRequest, db: Session = Depends(get_db)):
    """
    Core Aggregator Endpoint:
    Simulates searching the supplier network for available vehicles based on location and dates.
    """
    # For now, we query all vehicles marked as "Available" in the database.
    available_vehicles = db.query(models.Vehicle).filter(
        models.Vehicle.availability_status == "Available"
    ).all()

    if not available_vehicles:
        raise HTTPException(status_code=404, detail="No available vehicles found for this route.")

    return available_vehicles