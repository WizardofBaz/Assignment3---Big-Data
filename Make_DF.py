from Connection import get_redis_connection
import json
import pandas as pd

def get_data_from_redis(redis_client):
    """Pulls the data from the redis DB

    Args:
        redis_client (Any): The redis connection

    Returns:
        json data: The actual json data from the DB
    """    
    json_data = redis_client.get('api_data')
    if json_data:
        return json.loads(json_data)
    else:
        print("No JSON data found in Redis.")
        return None

if __name__ == "__main__":
    """Stores the data from the db to a pandas dataframe and then saves it as a .csv file
    """    
    r = get_redis_connection()
    data = get_data_from_redis(r)
    if data:
        df = pd.DataFrame(data)
        print("DataFrame created successfully:")
        print(df)
        #Saved to CSV top open in excel and decide what analysis to do.
        df.to_csv("Top_Stories_NYT.csv",index=False)
    else:
        print("Failed to get data from Redis.")