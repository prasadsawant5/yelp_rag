from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    user_id: str
    name: str
    review_count: int
    yelping_since: date
    friends: List[str]
    useful: int
    funny: int
    cool: int
    fans: int
    elite: List[int]
    average_stars: float
    compliment_more: float
    compliment_profile: float
    compliment_cute: float
    compliment_list: float
    compliment_note: float
    compliment_plain: float
    compliment_cool: float
    compliment_funny: float
    compliment_writer: float
    compliment_photos: float
