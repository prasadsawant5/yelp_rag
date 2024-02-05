from dataclasses import dataclass

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
    hours: dict
