import os
from dotenv import load_dotenv
load_dotenv()

TOKEN=os.getenv('TOKEN')
DB_PATH=os.getenv('DB_PATH')
DB_POST_PATH=os.getenv('DB_POST_PATH')
API_OPEN_AI=os.getenv('API_OPEN_AI')

INVITES_TO_POST=3

TIME_BEFORE_DELETING_WELCOME_MSG=10
TIME_BEFORE_DELETING_FAREWELL_MSG=10
TIME_BEFORE_DELETING_WARNING=10

__all__ = [
            "TOKEN",
            "DB_PATH",
            "DB_POST_PATH",
            "API_OPEN_AI",
            "INVITES_TO_POST",
            "TIME_BEFORE_DELETING_WELCOME_MSG",
            "TIME_BEFORE_DELETING_FAREWELL_MSG",
            "TIME_BEFORE_DELETING_WARNING"
          ]