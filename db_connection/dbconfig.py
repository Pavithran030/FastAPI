
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://postgres:redhat@localhost:5432/learn"
engine=create_engine(db_url)
session=sessionmaker(autocommit = False,autoflash = False,bind = engine)