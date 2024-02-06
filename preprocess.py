import psycopg2
import json
from tqdm import tqdm
from utils import *
from config import *

FILES = [
    'yelp_academic_dataset_business.json', 
    'yelp_academic_dataset_user.json',
    'yelp_academic_dataset_checkin.json', 
    'yelp_academic_dataset_review.json', 
    'yelp_academic_dataset_tip.json', 
]

def fix_parse_errors_in_json(file: str):
    with open(file, 'r', encoding='utf8') as f:
        lines = f.readlines()

    if lines[0].startswith('['):
        return
    
    n = len(lines)

    with open(file, 'w', encoding='utf8') as f:
        for i in tqdm(range(0, n)):
            line = lines[i]
            if i == 0:
                line = '[' + line
            
            if i == n - 1:
                line = line + ']'
            else:
                line = line.replace('\n', ', \n')

            lines[i] = line

        lines[-1] = lines[-1].replace(', \n', ']')

        f.writelines(lines)
            



def create_tables(conn: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor):
    try:
        for i in tqdm(range(0, len(TABLES))):
            cursor.execute(TABLES[i])
        conn.commit()
        print('*' * 30, end='')
        print(' Tables Created ', end='')
        print('*' * 30)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def execute_query(query: str, conn: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor):
    try:
        if query != None:
            query = query.replace('None', 'null')
            cursor.execute(query)
            conn.commit()
    except psycopg2.errors.SyntaxError as e:
        print()
        print(e)
        print(query)
        print()



if __name__ == '__main__':
    # for f in FILES:
    #     fix_parse_errors_in_json(f)

    print('*' * 28, end='')
    print(' JSON files fixed ', end='')
    print('*' * 28)

    conn = psycopg2.connect(f'dbname={DATABASE_NAME} user={USERNAME} password={PASSWORD}')

    cursor = conn.cursor()
    create_tables(conn, cursor)

    for file in FILES:
        try:
            f = open(file, 'r', encoding='utf8')
            data = json.load(f)

            for i in tqdm(range(0, len(data))):
                if '_business' in file:
                    b = data[i]
                    biz = convert_to_business_dto(b)
                    query = create_insert_business_query(biz)
                    execute_query(query, conn, cursor)
                    # print(query)
                    # break
                # elif '_user' in file:
                #     usr = data[i]
                #     user = convert_to_user_dto(usr)
                #     query = create_insert_user_query(user)
                #     execute_query(query, conn, cursor)
                #     # print(query)
                #     # break
                # elif '_review' in file:
                #     r = data[i]
                #     review = convert_to_review_dto(r)
                #     query = create_insert_review_query(review)
                #     execute_query(query, conn, cursor)
                #     # print(query)
                #     # break
                # elif '_checkin' in file:
                #     c = data[i]
                #     checkin = convert_to_checkin_dto(c)
                #     for _c in checkin:
                #         query = create_insert_checkin_query(_c)
                #         cursor.execute(query)
                #         conn.commit()
                #     #     print(query)
                #     # break
                # else:
                #     t = data[i]
                #     tip = convert_to_tip_dto(t)
                #     query = create_insert_tip_query(tip)
                #     execute_query(query, conn, cursor)
                #     # print(query)
                #     # break
            
            f.close()
        except json.decoder.JSONDecodeError as e:
            print(f'Error in decoding file {file}')
            print(e)


    cursor.close()
    conn.close()