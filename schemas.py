from pydantic import BaseModel, ConfigDict


class WorkerBase(BaseModel):
    role: str
    status: str = "Available"
    fatigue_score: float = 0.0


class WorkerCreate(WorkerBase):
    id: str


class WorkerResponse(WorkerBase):
    id: str
    model_config = ConfigDict(from_attributes=True)


class AGVBase(BaseModel):
    agv_type: str
    status: str = "Available"
    battery_pct: float = 100.0


class AGVCreate(AGVBase):
    id: str


class AGVResponse(AGVBase):
    id: str
    model_config = ConfigDict(from_attributes=True)