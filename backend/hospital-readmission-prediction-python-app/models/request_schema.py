from pydantic import BaseModel
from typing import Optional

class ReadmissionRequest(BaseModel):
    age: int
    diagnosis: str
    medications: int
    lab_result: float
    previous_admissions: int
    length_of_stay: int
    discharge_summary: str