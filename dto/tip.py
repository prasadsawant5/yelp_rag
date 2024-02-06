from dataclasses import dataclass
from datetime import date

@dataclass
class Tip:
    text: str
    date: date
    compliment_count: int
    business_id: str
    user_id: str