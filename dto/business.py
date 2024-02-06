from dataclasses import dataclass
from typing import List

@dataclass
class Business:
    business_id: str
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    latitude: float
    longitude: float
    stars: float
    review_count: float
    is_open: bool
    categories: List[str]
    monday_hours: str
    tuesday_hours: str
    wednesday_hours: str
    thursday_hours: str
    friday_hours: str
    satday_hours: str
    sunday_hours: str
