from dataclasses import dataclass
from typing import List

@dataclass
class Checkin:
    business_id: str
    date: List[str]