#!/usr/bin/python3

import os

os.environ["USER_FAVORITE_COLOR"] = input('What is your favorite color? ')
os.environ["USER_HOBBY"] = input('What is your favorite hobby? ')
os.environ["USER_CITY"] = input('What city do you live in? ')

print("Favorite Color:", os.getenv("USER_FAVORITE_COLOR"))
print("Hobby:", os.getenv("USER_HOBBY"))
print("City:", os.getenv("USER_CITY"))
