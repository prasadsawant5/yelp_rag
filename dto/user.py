from dataclasses import dataclass
from datetime import date
from typing import List

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
    compliment_hot: int
    compliment_more: int
    compliment_profile: int
    compliment_cute: int
    compliment_list: int
    compliment_note: int
    compliment_plain: int
    compliment_cool: int
    compliment_funny: int
    compliment_writer: int
    compliment_photos: int
