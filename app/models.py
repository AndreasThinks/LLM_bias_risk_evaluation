from pydantic import BaseModel
from enum import Enum


class RiskLevel(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

# Define your desired data structure.
class RiskAssessment(BaseModel):
    risk: str = RiskLevel