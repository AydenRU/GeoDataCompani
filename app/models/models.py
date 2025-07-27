from sqlalchemy import Table, Column, MetaData
from sqlalchemy import  Integer, String


metadata_db = MetaData()

users = Table(
    'users',
    metadata_db,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)