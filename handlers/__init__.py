from handlers.welcome_router import router as welcome_router
from handlers.anti_link      import router as link_router
from handlers.goodby_router  import router as farewell_router



__all__ = [
    "welcome_router",
    "link_router",
    "farewell_router",
    "advertisment_router"
    ]