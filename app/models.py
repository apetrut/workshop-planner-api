from datetime import datetime

from pydantic import BaseModel, Field


class WorkshopInput(BaseModel):
    title: str = Field(min_length=1)
    description: str
    startTime: datetime
    endTime: datetime
    organizerId: str = Field(min_length=1)
    status: str = Field(min_length=1)


class Workshop(WorkshopInput):
    id: str
