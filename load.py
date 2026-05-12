from sqlalchemy import create_engine

def save_to_db(df, db_name="weather_data.db", table_name="weather"):
    engine=create_engine(f'sqlite:///{db_name}')
    df.to_sql(table_name, con=engine, if_exists='append', index=False)