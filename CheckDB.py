from Connection import get_redis_connection
import json

def get_data_from_redis(data):
    json_data = data.get('api_data')
    if json_data:
        return json.loads(json_data)
    else:
        print("No data found in Redis.")
        return None

if __name__ == "__main__":
    r = get_redis_connection()
    redis_data = get_data_from_redis(r)
    if redis_data:
        print("Data retrieved from Redis:")
        print(redis_data)
    else:
        print("Failed to retrieve data from Redis.")
