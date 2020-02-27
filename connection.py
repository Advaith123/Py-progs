from sqlalchemy import create_engine, MetaData, Table, select, delete, insert
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import update

engine = create_engine('mysql+pymysql://root:root@localhost:3306/sakila')

metadata = MetaData()

actor = Table('Actor1', metadata, autoload=True, autoload_with = engine)

# class Example():
#     __tablename__ = 'Actor1'
#     actor_id = actor.Column('actor_id', actor.Integer, primary_key=True)
#     first_name = actor.Column('first_name', actor.String)
#     last_name = actor.Column('last_name', actor.String)
#
#     def __init__(self,actor_id,first_name,last_name):
#         self.actor_id = actor_id
#         self.first_name = first_name
#         self.last_name = last_name


print(actor.columns.keys())

connection = engine.connect()
stmt = select([actor])
#print(stmt)
result = connection.execute(stmt).fetchmany(size=11)
print(result)
stmt = delete([actor.columns[9]])
result = connection.execute(stmt).fetchmany(size=11)
print(result)
#

# for x in range (0, 10): ROW PROXY
#     for y in range (0, 4): DOES NOT
#         if result[x][y] == 'JOHNNY': SUPPORT ITEM
#             result[x][y] = 'JOHN'  ASSIGNMENT
connection = engine.connect()
stmt = select([actor])
# print(stmt)
result = connection.execute(stmt).fetchmany(size=10)
#
print(result)


# print(repr(actor))























# BASE = declarative_base()  # contains configs
#
# class Custmor(BASE):
#     __tablename__ = "Custmor"
#     id = Column(Integer, primary_key = True)
#     name = Column(String(200))
#     age = Column(Integer)
#     def __str__(self): #object
#         return self.name
#
# BASE.metadata.create_all(ENGINE)
# from sqlalchemy import create_engine
# DB_URL = 'mysql+MySQLdb://root:root@localhost:3306/employee'
# ENGINE = create_engine(DB_URL)
# conn = ENGINE.connect()
# try:
#     print('your connection ok')
# except:
#     print('your connection not connected')
