# main.py
from RedisCheck_Class import RedisKeyChecker

def main():
    key_checker = RedisKeyChecker()

    key_to_check = "name"

    # Check if the key exists in the Redis database
    key_checker.check_key(key_to_check)

if __name__ == "__main__":
    main()
