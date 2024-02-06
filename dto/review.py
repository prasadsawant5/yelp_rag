from dataclasses import dataclass
from datetime import date

@dataclass
class Review:
    review_id: str
    user_id: str
    business_id: str
    stars: int
    date: date
    text: str
    useful: int
    funny: int
    cool: int