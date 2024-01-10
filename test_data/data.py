import os
from dotenv import load_dotenv

load_dotenv()


class Data:

    DEFAULT_USER_1 = {'login': 'autoTestSpecialist@brainup.spb.ru',
                      'password': 'password'}  # default user with limited access
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    DEFAULT_USER_2 = {'login': 'default@default.ru', 'password': 'password'}  # default user with limited access
