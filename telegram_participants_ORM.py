
# coding: utf-8

# In[22]:


#테이블 생성

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:zikto430@db.zikto.com/zikto_db_test', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String 

class telegram_table(Base):
    __tablename__ = 'telegram_participants'
    date = Column(String(50), primary_key = True)
    participants = Column(Integer)
    def __init__(self, date, participants):
        self.date = date
        self.participants = participants
    def __repr__(self, date, participants):
        return "<telegram_table('%s', '%d')>" % (self.date, self.participants)
Base.metadata.create_all(engine)


# In[23]:


# 데이터 입력

import requests, json, time, datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:zikto430@db.zikto.com/zikto_db_test', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# In[25]:


true = 'true'
false = 'false'
telegram_url = 'https://api.telegram.org/bot579221882:AAF_c4tT17EkEjiNHFswxxWlQZmba2TUO7Y/getChatMembersCount?chat_id=-1001235789611'
r = requests.get(telegram_url)
data_received = r.json()
today = datetime.datetime.today().strftime('%Y-%m-%d')
date=today
participants = int(data_received['result'])
new_date = telegram_table(date,participants)

session.add(new_date)
session.commit()

