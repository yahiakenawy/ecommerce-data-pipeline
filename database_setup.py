import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, String, MetaData, Table
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "sqlite:///books.db"

def create_database(csv_file="clean_books.csv"):
    # Read cleaned data
    df = pd.read_csv(csv_file)
    
    # Create SQLAlchemy engine
    engine = create_engine(DATABASE_URI, echo=True)
    metadata = MetaData()

    # Define table schema
    books_table = Table('books', metadata,
                        Column('id', Integer, primary_key=True, autoincrement=True),
                        Column('title', String),
                        Column('price', Float),
                        Column('rating', String),
                        Column('rating_num', Integer),
                        Column('availability', String)
                       )

    # Create the table
    metadata.drop_all(engine)  # Remove old tables if exist
    metadata.create_all(engine)

    # Insert data into the table
    df.to_sql('books', con=engine, if_exists='append', index=False)
    print("Database setup complete. Data inserted into books.db.")

if __name__ == "__main__":
    create_database()