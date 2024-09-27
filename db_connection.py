from sqlalchemy import create_engine

def get_db_engine():
    # Define your database credentials
    db_username = 'postgres'
    db_password = '17Sichdama!'
    db_host = 'localhost'
    db_port = '5432'
    db_name = 'mydatabase'

    # Create and return the engine
    engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
    return engine
