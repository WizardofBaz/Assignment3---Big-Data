#Get's the data from an API and stores into our Redis DB

import requests
import redis
import os

from redis.exceptions import ResponseError
from Connection import get_redis_connection
from dotenv import load_dotenv, find_dotenv
from pynytimes import NYTAPI

### give the full path 
path= r'C:\Users\arbaz\Documents\Masters\Big Data\Assignment3\API_KEY.env'

load_dotenv(dotenv_path=path,verbose=True)
API_KEY = os.getenv("API_KEY")

r = get_redis_connection()
r.flushall()


api_key = API_KEY
nyt = NYTAPI(api_key, parse_dates=True)

def get_data_from_api():
    top_stories = nyt.top_stories()
    top_story = top_stories[0]
    #print(top_story)

def insert_into_redis(data):
    try:
        for item in data:
            key = f"data:{item['id']}"
            r.jsonset(key, '.', item)
            print("Inserted:", key)
    except ResponseError as e:
        print("RedisJSON Error:", e)

if __name__ == "__main__":
    #get data from API
    api_data = get_data_from_api()
    if api_data:
        insert_into_redis(api_data)
