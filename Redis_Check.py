# main.py
from Redis_Check import RedisKeyChecker

def main():
    key_checker = RedisKeyChecker()

    key_to_check = "api_data"

    # Check if the key exists in the Redis database
    key_checker.check_key(key_to_check)

if __name__ == "__main__":
    main()
