from dataclasses import dataclass
import datetime

@dataclass
class Checkin:
    business_id: str
    date: datetime