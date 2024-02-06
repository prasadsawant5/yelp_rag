from typing import List
from datetime import datetime
from dto.business import Business
from dto.checkin import Checkin
from dto.review import Review
from dto.tip import Tip
from dto.user import User

def convert_to_business_dto(d: dict) -> Business:
    return Business(
        d['business_id'], d['name'], d['address'], d['city'], d['state'], d['postal_code'], d['latitude'], d['longitude'], 
        d['stars'], d['review_count'], True if d['is_open'] == 1 else False, d['categories'].split(','), d['hours']
    )

def convert_to_user_dto(d: dict) -> User:
    return User(
        d['user_id'], d['name'], d['review_count'], d['yelping_since'], d['friends'], d['useful'], d['funny'], d['cool'], d['fans'], 
        d['elite'], d['average_stars'], d['compliment_more'], d['compliment_profile'], d['compliment_cute'],d['compliment_list'], d['compliment_note'], 
        d['compliment_plain'], d['compliment_cool'], d['compliment_funny'], d['compliment_writer'], d['compliment_photos']
    )

def convert_to_review_dto(d: dict) -> Review:
    return Review(
        d['review_id'], d['user_id'], d['business_id'], d['stars'], d['date'], d['text'], d['useful'], d['funny'],d['cool']
    )

def convert_to_tip_dto(d: dict) -> Tip:
    return Tip(
        d['text'], d['date'], d['compliment_count'], d['business_id'], d['user_id']
    )

def convert_to_checkin_dto(d: dict) -> List[Checkin]:
    dates = d['date'].split(',')
    biz_id = d['business_id']
    checkins = []

    for d in dates:
        dt = datetime.strptime(d, '%y/%m/%d %H:%M:%S')
        checkins.append(Checkin(biz_id, dt))

    return checkins

def create_insert_business_query(biz: Business) -> str:
    return f'''
        INSERT INTO businesses (business_id, name, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open, categories, hours) 
        VALUES (\'{biz.business_id}\', \'{biz.name}\', \'{biz.address}\', \'{biz.city}\', \'{biz.state}\', \'{biz.postal_code}\', {biz.latitude}, {biz.longitude}, {biz.stars}, {biz.review_count}, {biz.is_open}, ARRAY[{get_categories(biz.categories)}], {biz.hours})
    '''

def create_insert_user_query(usr: User) -> str:
    return f'''
        INSERT INTO users (user_id, name, review_count, yelping_since, friends, useful, funny, cool, fans, elite, average_stars, compliment_hot, compliment_more, compliment_profile, compliment_cute, compliment_list, compliment_note, compliment_plain, compliment_cool, compliment_funny, compliment_writer, compliment_photos) 
        VALUES (\'{usr.user_id}\', \'{usr.name}\', \'{usr.review_count}\', \'{usr.yelping_since}\', ARRAY[{get_categories(usr.friends)}], \'{usr.useful}\', {usr.funny}, {usr.cool}, {usr.fans}, ARRAY[{get_categories(usr.elite)}], {usr.average_stars}, {usr.compliment_hot}, {usr.compliment_more}, {usr.compliment_profile}, {usr.compliment_cute}, {usr.compliment_list}, 
        {usr.compliment_note}, {usr.compliment_plain}, {usr.compliment_cool}, {usr.compliment_funny}, {usr.compliment_writer}, {usr.compliment_photos})
    '''

def get_categories(categories: List[str]) -> str:
    s = ''
    for i in range(0, len(categories)):
        s += '\'' + categories[i] + '\''
        if i != len(categories) - 1:
            s += ', '

    return s