import random
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base, engine, SessionLocal


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    integration_type = Column(String)
    reliability_score = Column(Float)
    esg_rating = Column(String)

    assets = relationship("FleetAsset", back_populates="supplier", cascade="all, delete-orphan")


class FleetAsset(Base):
    __tablename__ = "fleet_assets"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    asset_class = Column(String)
    available_capacity = Column(Integer)
    unit_cost_eur = Column(Float)
    carbon_footprint_kg_per_km = Column(Float)
    is_active = Column(Boolean, default=True)
    last_telemetry_update = Column(DateTime, default=datetime.utcnow)

    supplier = relationship("Supplier", back_populates="assets")


def hydrate_database():
    print("Initializing Neon database schema...")

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        modern_supplier_1 = Supplier(
            name="EuroFreight Digital (API)", integration_type="Modern B2B (API)", reliability_score=99.8,
            esg_rating="AAA"
        )
        legacy_supplier_1 = Supplier(
            name="Oceanus Inland Logistics (RPA)", integration_type="Legacy Carrier (RPA)", reliability_score=92.5,
            esg_rating="B"
        )
        modern_supplier_2 = Supplier(
            name="GreenRail Intermodal (API)", integration_type="Modern B2B (API)", reliability_score=98.0,
            esg_rating="AAA"
        )

        db.add_all([modern_supplier_1, legacy_supplier_1, modern_supplier_2])
        db.commit()

        assets = [
            FleetAsset(supplier_id=modern_supplier_1.id, asset_class="Volvo FH Electric Truck", available_capacity=15,
                       unit_cost_eur=180.0, carbon_footprint_kg_per_km=0.15),
            FleetAsset(supplier_id=modern_supplier_1.id, asset_class="Euro 6 Heavy Duty LCV", available_capacity=42,
                       unit_cost_eur=145.0, carbon_footprint_kg_per_km=0.85),
            FleetAsset(supplier_id=legacy_supplier_1.id, asset_class="Standard 40ft TEU Container",
                       available_capacity=120, unit_cost_eur=85.0, carbon_footprint_kg_per_km=1.20),
            FleetAsset(supplier_id=legacy_supplier_1.id, asset_class="Diesel Drayage Truck", available_capacity=8,
                       unit_cost_eur=110.0, carbon_footprint_kg_per_km=1.50),
            FleetAsset(supplier_id=modern_supplier_2.id, asset_class="Block Train Cargo Slot", available_capacity=300,
                       unit_cost_eur=65.0, carbon_footprint_kg_per_km=0.25),
            FleetAsset(supplier_id=modern_supplier_2.id, asset_class="Refrigerated Rail Car", available_capacity=25,
                       unit_cost_eur=95.0, carbon_footprint_kg_per_km=0.35),
        ]

        for _ in range(20):
            assets.append(
                FleetAsset(
                    supplier_id=random.choice([modern_supplier_1.id, legacy_supplier_1.id]),
                    asset_class="Spot Market 20ft Container",
                    available_capacity=random.randint(5, 50),
                    unit_cost_eur=round(random.uniform(70.0, 130.0), 2),
                    carbon_footprint_kg_per_km=round(random.uniform(0.9, 1.4), 2)
                )
            )

        db.add_all(assets)
        db.commit()

        print(
            f"Hydration Complete: {db.query(Supplier).count()} Suppliers, {db.query(FleetAsset).count()} Assets seeded.")

    except Exception as e:
        db.rollback()
        print(f"Hydration Failed: {str(e)}")
    finally:
        db.close()


if __name__ == "__main__":
    hydrate_database()