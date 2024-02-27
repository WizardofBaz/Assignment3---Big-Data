from Connection import get_redis_connection

"""Checking to make sure that the redis connection is correct and working
"""
r = get_redis_connection()

r.flushall()

## Store a String Key
r.set("name", "Baz")

## Display the Data Type
print(r.type("name"))

## Retrive the String Key
print(r.get("name"))