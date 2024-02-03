from decouple import config
import datetime
from peewee import *

db_config = {
  'user': config('DB_USER'),
  'password': config('DB_PWD'),
  'host': config('DB_HOST'),
  'database': config('DB'),
}

db = MySQLDatabase(**db_config)

class BaseModel(Model):
  class Meta:
    database = db
    
class User(BaseModel):
  id = BigAutoField(unique=True)
  username = CharField(null=True)
  first_name = CharField(null=True)
  last_name = CharField(null=True)
  chat_id = BigIntegerField()
  reg_date = DateTimeField()
  
  class Meta: 
    table_name = 'User'

class Test(BaseModel):
  user = ForeignKeyField(User)
  leader = IntegerField()
  shaman = IntegerField()
  worker = IntegerField()
  warrior = IntegerField()
  dealer = IntegerField()
  researcher = IntegerField()
  artist = IntegerField()
  date = DateTimeField()
  
  class Meta:
    table_name = 'Test'

# Create Tables
with db:
  db.create_tables([User, Test], safe=True)

db.close()


#  utils
@db.connection_context()
def create_user(id: int, username: str, first_name: str, last_name: str, chat_id: int) -> None:
  User.create(id=id, username=username, first_name=first_name, last_name=last_name, chat_id=chat_id, reg_date=datetime.datetime.utcnow())

@db.connection_context()
def create_test(user_id: int, leader: int, shaman: int, worker: int, warrior: int, dealer: int, researcher: int, artist: int) -> None:
  user = User.get(User.id == user_id)
  Test.create(user=user, leader=leader, shaman=shaman, worker=worker, warrior=warrior, dealer=dealer, researcher=researcher, artist=artist, date=datetime.datetime.utcnow())
 
@db.connection_context() 
def user_exists(user_id: int) -> bool:
  try:
    User.get_by_id(user_id)
    return True
  except DoesNotExist:
    return False
