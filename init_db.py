from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
import datetime

engine = create_engine('postgres+psycopg2://postgres:231234@127.0.0.1:5432/')
conn = engine.connect()
conn.execute("commit")
#todo: refactor code below
conn.execute("DROP DATABASE IF EXISTS comeunitydb;")
conn.execute("commit")

conn.execute("CREATE DATABASE comeunitydb;")
conn.execute("commit")

conn.close()
engine = create_engine('postgres+psycopg2://postgres:postgres@127.0.0.1:5432/comeunitydb')
metadata = MetaData()
user = Table('users', metadata,
             Column('id', Integer, primary_key=True, autoincrement=True),
             Column('user_name', String(25), nullable=False, unique=True),
             Column('user_email', String(35), nullable=False, unique=True),
             Column('user_password', String(255), nullable=False),
             Column('user_first_name', String(25), nullable=False),
             Column('user_last_name', String(25), nullable=False),
             Column('user_image_file', String(25), nullable=False),
             Column('user_registration_data', DateTime, nullable=False, default=datetime.datetime.now())
)
user.create(engine)
