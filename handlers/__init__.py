from handlers.welcome_router import router  as welcome_router
from handlers.anti_link      import router  as antispam_router
from handlers.goodby_router  import router  as farewell_router
from handlers.del_sys_msg    import router  as del_tg_msg_router
from handlers.del_sys_msg    import router_ as del_pers_msgs_router



__all__ = [
    "welcome_router",
    "antispam_router",
    "farewell_router",
    "del_tg_msg_router",
    "del_pers_msgs_router"
    ]