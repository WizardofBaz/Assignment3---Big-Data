# main.py
from RedisCheck_Class import RedisKeyChecker

def main():
    """From the RedisCheck_Class I just check to see that the key I'm searching for is in the Redis DB
    """    
    key_checker = RedisKeyChecker()

    key_to_check = "api_data"

    # Check if the key exists in the Redis database
    key_checker.check_key(key_to_check)

if __name__ == "__main__":
    main()
