from typing import List
from datetime import datetime
from dto.business import Business
from dto.checkin import Checkin
from dto.review import Review
from dto.tip import Tip
from dto.user import User

def convert_to_business_dto(d: dict) -> Business:
    try:
        return Business(
            d['business_id'], d['name'], d['address'], d['city'], d['state'], d['postal_code'], d['latitude'], d['longitude'], 
            d['stars'], d['review_count'], True if d['is_open'] == 1 else False, d['categories'].split(',') if d['categories'] != None else None, 
            d['hours']['Monday'] if d['hours'] != None and 'Monday' in d['hours'].keys() else None, 
            d['hours']['Tuesday'] if d['hours'] != None and 'Tuesday' in d['hours'].keys() else None, 
            d['hours']['Wednesday'] if d['hours'] != None and 'Wednesday' in d['hours'].keys() else None, 
            d['hours']['Thursday'] if d['hours'] != None and 'Thursday' in d['hours'].keys() else None, 
            d['hours']['Friday'] if d['hours'] != None and 'Friday' in d['hours'].keys() else None, 
            d['hours']['Saturday'] if d['hours'] != None and 'Saturday' in d['hours'].keys() else None, 
            d['hours']['Sunday'] if d['hours'] != None and 'Sunday' in d['hours'].keys() else None, 
        )
    except KeyError as e:
        print(e)
        print(d)

def convert_to_user_dto(d: dict) -> User:
    try:
        return User(
            d['user_id'], d['name'], d['review_count'], d['yelping_since'], d['friends'].split(',') if d['friends'] != None else None, d['useful'], d['funny'], d['cool'], d['fans'], 
            d['elite'].split(',') if d['elite'] != None else None, d['average_stars'], d['compliment_hot'], d['compliment_more'], d['compliment_profile'], d['compliment_cute'],d['compliment_list'], d['compliment_note'], 
            d['compliment_plain'], d['compliment_cool'], d['compliment_funny'], d['compliment_writer'], d['compliment_photos']
        )
    except KeyError as e:
        print(e)
        print(d)

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
        d = d.lstrip()
        d = d.rstrip()
        dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        checkins.append(Checkin(biz_id, dt))

    return checkins

def create_insert_business_query(biz: Business) -> str:
    try:
        return f'''
            INSERT INTO businesses (business_id, name, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open, categories, monday_hours, tuesday_hours, wednesday_hours, thursday_hours, friday_hours, satday_hours, sunday_hours) 
            VALUES ('{biz.business_id}', '{biz.name.replace("'", "")}', '{biz.address.replace("'", "")}', '{biz.city.replace("'", "")}', '{biz.state}', '{biz.postal_code}', {biz.latitude}, {biz.longitude}, {biz.stars}, {biz.review_count}, {biz.is_open}, {'ARRAY[' + get_categories(biz.categories) + ']' if biz.categories != None and len(biz.categories) > 0 else 'null'}, 
            '{biz.monday_hours}', '{biz.tuesday_hours}', '{biz.wednesday_hours}', '{biz.thursday_hours}', '{biz.friday_hours}', '{biz.satday_hours}', '{biz.sunday_hours}')
        '''
    except Exception as e:
        print()
        print(biz)
        print(e)
        print()

def create_insert_user_query(usr: User) -> str:
    return f'''
        INSERT INTO users (user_id, name, review_count, yelping_since, friends, useful, funny, cool, fans, elite, average_stars, compliment_hot, compliment_more, compliment_profile, compliment_cute, compliment_list, compliment_note, compliment_plain, compliment_cool, compliment_funny, compliment_writer, compliment_photos) 
        VALUES ('{usr.user_id}', '{usr.name.replace("'", "")}', {usr.review_count}, '{usr.yelping_since}', ARRAY[{get_categories(usr.friends)}], {usr.useful}, {usr.funny}, {usr.cool}, {usr.fans}, ARRAY[{get_categories(usr.elite)}], {usr.average_stars}, {usr.compliment_hot}, {usr.compliment_more}, {usr.compliment_profile}, {usr.compliment_cute}, {usr.compliment_list}, 
        {usr.compliment_note}, {usr.compliment_plain}, {usr.compliment_cool}, {usr.compliment_funny}, {usr.compliment_writer}, {usr.compliment_photos})
    '''

def create_insert_review_query(r: Review) -> str:
    return f'''
        INSERT INTO reviews (review_id, user_id, business_id, stars, date, text, useful, funny, cool) 
        VALUES ('{r.review_id}', '{r.user_id}', '{r.business_id}', {r.stars}, '{r.date}', '{r.text.replace("'", "")}', {r.useful}, {r.funny}, {r.cool})
    '''

def create_insert_checkin_query(c: Checkin) -> str:
    return f'''
        INSERT INTO checkins (business_id, date) VALUES ('{c.business_id}', '{c.date}')
    '''

def create_insert_tip_query(tip: Tip) -> str:
    return f'''
        INSERT INTO tips (text, date, compliment_count, business_id, user_id) 
        VALUES ('{tip.text.replace("'", "")}', '{tip.date}', {tip.compliment_count}, '{tip.business_id}', '{tip.user_id}')
    '''

def get_categories(categories: List[str]) -> str:
    s = ''
    if categories != None:
        for i in range(0, len(categories)):
            s += '\'' + categories[i].replace("'", "") + '\''
            if i != len(categories) - 1:
                s += ', '

    return s
