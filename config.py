import os
user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
DATABASE_CONNECTION_URI=f'postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}'