PROMPT_TEMPLATE=""" You are a chat moderator.

    Return 1 if the message is a real commercial advertisement 
    
    (selling, buying, promoting goods/services, business offer, prices, contact for business).
    
    Return 0 otherwise.

    Only output 1 or 0.

    Text:
    """
    
CREATE_DB_FOR_USERS="""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY, 
                username TEXT,
                invitor_id INTEGER,
                invite_counts INTEGER DEFAULT 0,
                posts INTEGER DEFAULT 0,
                created_at TEXT DEFAULT (date('now'))  
            ) 
            """
            
CREATE_DB_FOR_POSTS="""
            CREATE TABLE IF NOT EXISTS post (
                user_id INTEGER PRIMARY KEY, 
                posts INTEGER DEFAULT 0
            ) 
            """

SQL_INSERT_USER_IN_DB_USERS = """
                                INSERT 
                                     OR 
                                IGNORE 
                                     INTO 
                                        users (user_id, username) 
                                    VALUES (?, ?)
                              """
                                              
SQL_INSERT_USER_IN_DB_POSTS = """
                                INSERT 
                                     OR 
                                IGNORE 
                                     INTO 
                                        post (user_id) 
                                    VALUES (?)
                              """

SQL_IS_IN_DB_CHECK = """
                       SELECT 
                             1 
                       FROM 
                            users 
                       WHERE 
                            user_id = ?
                    """

SQL_INVITES_COUNT="""
                    SELECT
                        invite_counts 
                    FROM 
                        users 
                    WHERE 
                        user_id = ?;
                """

SQL_POST_COUNT="""
                 SELECT
                      posts 
                 FROM 
                      post 
                 WHERE 
                      user_id = ?;
               """

SQL_UPDATE_PLUS_ONE_INVITE="""
                            UPDATE 
                                users 
                            SET 
                                invite_counts = invite_counts + 1 
                            WHERE 
                                user_id = ?
                        """

SQL_UPDATE_PLUS_ONE_POST="""
                            UPDATE 
                                post 
                            SET 
                                posts = posts + 1 
                            WHERE 
                                user_id = ?
                        """

WELCOME_MESSAGE_FOR_NEW = """
Вітаємо, {first_name}, у чаті {chat_name}! 👋\n\n"
Будь ласка, ознайомтеся з правилом📌: 
Щоб опублікувати 1-ну публікацію - запросіть 3х друзів😸
"""

WELCOME_MESSAGE_FOR_OLD = """
З поверненням, {first_name}! 
Раді Вас знову бачити у чаті {chat_name}!👋
"""

GOODBY_MESSAGE="""
{first_name} покинув чат 😒 \nСподіваємось на Ваше повернення😄
"""

FORWARDED_FROM_CHANELS_PROHIBITED="""
{first_name}, повідомлення видалено. Причина:\nПереслані повідомлення з каналів заборонені❌
"""

LINKS_PROHIBITED="""
{first_name}, повідомлення видалено. Причина:\n Скидати посилання в чат заборонено❌
"""

THANKS_FOR_POST="""
{first_name}, дякуємо за пост😃\n Щоб зробити настпуний - запросіть ще 3х людей в чат😎'
"""

SORRY_YOU_CANT_POST="""
{first_name}, повідомлення видалено. Причина:
Нажаль Ви не маєте права на пост, бо не запросили достатньо людей☹ 
Пам'ятайте - кожен пост коштує 3 запрошення😁
"""