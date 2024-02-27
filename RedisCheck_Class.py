from Connection import get_redis_connection

class RedisKeyChecker:
    def __init__(self):
        r = get_redis_connection()
        self.redis_client = r

    def check_key(self, key):
        if self.redis_client.exists(key):
            print(f"The key '{key}' exists in the Redis database.")
        else:
            print(f"The key '{key}' does not exist in the Redis database.")
