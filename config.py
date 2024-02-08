DATABASE_NAME='yelp'
USERNAME='prasad'
PASSWORD='password'

TABLES = (
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
        stars FLOAT, 
        review_count INT, 
        is_open BOOLEAN NOT NULL, 
        categories TEXT[], 
        monday_hours TEXT, 
        tuesday_hours TEXT, 
        wednesday_hours TEXT, 
        thursday_hours TEXT, 
        friday_hours TEXT, 
        satday_hours TEXT, 
        sunday_hours TEXT
    )
    ''', 

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
        id SERIAL PRIMARY KEY, 
        business_id VARCHAR(22) NOT NULL REFERENCES businesses (business_id), 
        date TIMESTAMP[]
    )
    ''', 

    '''
    CREATE TABLE tips (
        id SERIAL PRIMARY KEY, 
        text TEXT NOT NULL, 
        date DATE, 
        compliment_count INT, 
        business_id VARCHAR(22) NOT NULL REFERENCES businesses (business_id), 
        user_id VARCHAR(22) NOT NULL REFERENCES users (user_id)
    )
    '''
)

ABSENT_ENTITIES = [
    'tquAg8GqbhN5k6Hkd23M0A', '5iBVQ3OeK8lV4Z_4PXc1Xw', 'u8cq-5zzD7dPSa3LR8rIMw', '433BzxUeQAmRmK0g06UAfA', 'dWZlWFtsEXFVq_vulT00lA', 'sxxnBQb15fOyg30JInIKqw', 
    'MaengE6zJ6k_d5e6nwnVaA', '5XiPz5mJK_RtJQVkXIqxYg', 'I200IyE9DCxJvvof2wnO6A', 'G0PWeUgNeGDobntevJlJ1g', '0oMk8hhMqiSt4G1BJjjG6g', 'vq2H7lJ73VwXMDqC8DiImw', 
    'lzpM_Vf2rKA4ivGtAIOH4w', 'qH_QwXBgA4Z7WyCjtwRi2A', '3N6-acEgosQSbipmBZKoSg', 'ufZfni7nb_KdJC6DXNfVHQ', 'VTfl9PALOCiGV8SUBpCZEQ', 'UwaRBUSj45sE9_kAnaGggw', 
    'AQnEwfNAgdxqRWpia__syA', '77n3enAMdlka0pZ82GT9VQ', 'NCeW1I6C4K7qhY4kRH8cOA', 'I6tb6vPxJ8Tct79JgqIDrQ', 'U76IFozArZsShdmoIdDMUw', 'lzpM_Vf2rKA4ivGtAIOH4w', 
    'QLU-88WwG4hKj6jKSR8iig', 'EkUWydx3bJmiMWOBmdVf4Q', 'OxvEeexqWWeWkPwkKtTy2Q', '5-L9Oo6PyUiBjeqj1GsJyQ', '4bqSo-Xfd8Yu5BMDsd947Q', 'PCS3F53ltR_svcnncSw6pw', 
    'Qt6BEJjT05S-HCYKIS45dQ', 'b4QR6E98D4-xYBNFPWZEvg', 'I6G8wz_LD_8IsCPxvjs8SQ'
]