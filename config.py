DATABASE_NAME='yelp'
USERNAME='postgres'
PASSWORD='password'

TABLES = (
    # '''
    # CREATE TABLE businesses (
    #     business_id VARCHAR(22) PRIMARY KEY NOT NULL, 
    #     name TEXT NOT NULL, 
    #     address TEXT NOT NULL, 
    #     city TEXT NOT NULL, 
    #     state TEXT NOT NULL, 
    #     postal_code TEXT NOT NULL, 
    #     latitude DOUBLE PRECISION, 
    #     longitude DOUBLE PRECISION, 
    #     stars FLOAT, 
    #     review_count INT, 
    #     is_open BOOLEAN NOT NULL, 
    #     categories TEXT[], 
    #     monday_hours TEXT, 
    #     tuesday_hours TEXT, 
    #     wednesday_hours TEXT, 
    #     thursday_hours TEXT, 
    #     friday_hours TEXT, 
    #     satday_hours TEXT, 
    #     sunday_hours TEXT
    # )
    # ''', 

    '''
    CREATE TABLE users (
        user_id VARCHAR(22) PRIMARY KEY NOT NULL, 
        name TEXT NOT NULL, 
        review_count INT, 
        yelping_since DATE, 
        friends TEXT[], 
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

    # '''
    # CREATE TABLE reviews (
    #     review_id VARCHAR(22) PRIMARY KEY NOT NULL, 
    #     user_id VARCHAR(22) NOT NULL REFERENCES users (user_id), 
    #     business_id VARCHAR(22) NOT NULL REFERENCES businesses (business_id), 
    #     stars INT NOT NULL, 
    #     date DATE NOT NULL, 
    #     text TEXT NOT NULL, 
    #     useful INT, 
    #     funny INT, 
    #     cool INT
    # )
    # ''', 

    # '''
    # CREATE TABLE checkins (
    #     business_id VARCHAR(22) NOT NULL REFERENCES businesses (business_id), 
    #     date DATE
    # )
    # ''', 

    # '''
    # CREATE TABLE tips (
    #     id SERIAL PRIMARY KEY, 
    #     text TEXT NOT NULL, 
    #     date DATE, 
    #     compliment_count INT, 
    #     business_id VARCHAR(22) NOT NULL REFERENCES businesses (business_id), 
    #     user_id VARCHAR(22) NOT NULL REFERENCES users (user_id)
    # )
    # '''
)