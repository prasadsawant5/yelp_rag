import psycopg2
import json
from tqdm import tqdm

FILES = [
    'yelp_academic_dataset_business.json', 
    'yelp_academic_dataset_checkin.json', 
    'yelp_academic_dataset_review.json', 
    'yelp_academic_dataset_tip.json', 
    'yelp_academic_dataset_user.json'
]

def fix_parse_errors_in_json(file: str):
    with open(file, 'r') as f:
        lines = f.readlines()

    if lines[0].startswith('['):
        return

    with open(file, 'w') as f:
        for i in tqdm(range(0, len(lines))):
            line = lines[i]
            if i == 0:
                line = '[' + line

            line = line.replace('\n', ', \n')

            lines[i] = line

        lines[-1] = lines[-1] + ']'

        f.writelines(lines)
            



def create_tables(conn: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor):
    tables = (
        '''
        CREATE TABLE businesses (
            business_id VARCHAR(22) PRIMARY KEY NOT NULL, 
            name TEXT NOT NULL, 
            address TEXT NOT NULL, 
            city TEXT NOT NULL, 
            state TEXT NOT NULL, 
            postal_code TEXT NOT NULL, 
            latitude DOUBLE PRECISION, 
            longitude DOUBLE PRECISION, 
            stars NUMERIC(1, 1), 
            review_count INT, 
            is_open BOOLEAN NOT NULL, 
            categories TEXT[], 
            hours JSON
        )
        ''', 

        '''
        CREATE TABLE users (
            user_id VARCHAR(22) PRIMARY KEY NOT NULL, 
            name TEXT NOT NULL, 
            review_count INT, 
            yelping_since DATE, 
            friends VARCHAR(22)[], 
            useful INT, 
            funny INT, 
            cool INT, 
            fans INT, 
            elite INT[], 
            average_stars FLOAT, 
            compliment_hot INT, 
            compliment_more INT, 
            compliment_profile INT, 
            compliment_cute INT, 
            compliment_list INT, 
            compliment_note INT, 
            compliment_plain INT, 
            compliment_cool INT, 
            compliment_funny INT, 
            compliment_writer INT, 
            compliment_photos INT
        )
        ''', 

        '''
        CREATE TABLE reviews (
            review_id VARCHAR(22) PRIMARY KEY NOT NULL, 
            user_id VARCHAR(22) NOT NULL REFERENCES users (user_id), 
            business_id VARCHAR(22) NOT NULL REFERENCES businesses (business_id), 
            stars INT NOT NULL, 
            date DATE NOT NULL, 
            text TEXT NOT NULL, 
            useful INT, 
            funny INT, 
            cool INT
        )
        ''', 

        '''
        CREATE TABLE checkins (
            business_id VARCHAR(22) NOT NULL REFERENCES businesses (business_id), 
            date DATE
        )
        ''', 

        '''
        CREATE TABLE tips (
            text TEXT NOT NULL, 
            date DATE, 
            compliment_count INT, 
            business_id VARCHAR(22) NOT NULL REFERENCES businesses (business_id), 
            user_id VARCHAR(22) NOT NULL REFERENCES users (user_id)
        )
        '''
    )

    try:
        for i in tqdm(range(0, len(tables))):
            cursor.execute(tables[i])
        # conn.commit()
        print('*' * 30, end='')
        print(' Tables Created ', end='')
        print('*' * 30)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



if __name__ == '__main__':
    # for f in FILES:
    #     fix_parse_errors_in_json(f)

    print('*' * 25, end='')
    print(' JSON files fixed ', end='')
    print('*' * 25)

    conn = psycopg2.connect('dbname=yelp user=prasad password=password')

    cursor = conn.cursor()
    # create_tables(cursor)

    f = open(FILES[0])
    businesses = json.load(f)

    for i in tqdm(range(0, len(businesses))):
        b = businesses[i]

    cursor.close()
    conn.close()