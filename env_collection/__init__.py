import os
from dotenv import load_dotenv
load_dotenv()

TOKEN=os.getenv('TOKEN')
DB_PATH=os.getenv('DB_PATH')
DB_POST_PATH=os.getenv('DB_POST_PATH')
API_OPEN_AI=os.getenv('API_OPEN_AI')
INVITES_TO_POST=int(os.getenv('INVITES_TO_POST'))
TIME_BEFORE_DELETING_WELCOME_MSG=int(os.getenv('TIME_BEFORE_DELETING_WELCOME_MSG'))
TIME_BEFORE_DELETING_FAREWELL_MSG=int(os.getenv('TIME_BEFORE_DELETING_FAREWELL_MSG'))
TIME_BEFORE_DELETING_WARNING=int(os.getenv('TIME_BEFORE_DELETING_WARNING'))

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

