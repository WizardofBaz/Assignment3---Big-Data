#Get's the data from an API and stores into our Redis DB
import os
import json
from datetime import datetime

from redis.exceptions import ResponseError
from Connection import get_redis_connection
from dotenv import load_dotenv, find_dotenv
from pynytimes import NYTAPI

### give the full path 
path= r'C:\Users\arbaz\Documents\Masters\Big Data\Assignment3\API_KEY.env'

load_dotenv(dotenv_path=path,verbose=True)
API_KEY = os.getenv("API_KEY")

api_key = API_KEY
nyt = NYTAPI(api_key, parse_dates=True)

def get_data_from_api():
    top_stories = nyt.top_stories()  
    top_stories = top_stories[:10]
    #print(top_story)
    return top_stories  

def insert_into_redis(data):
    api_data = get_data_from_api()
    if api_data:
        for story in api_data:
            for key, value in story.items():
                if isinstance(value, datetime):
                    story[key] = value.isoformat()
        data.set('api_data', json.dumps(api_data))
        print("JSON data stored in Redis successfully.")
    else:
        print("Failed to get API data.")

if __name__ == "__main__":
    # Connect to Redis
    r = get_redis_connection()
    r.flushall()
    insert_into_redis(r)