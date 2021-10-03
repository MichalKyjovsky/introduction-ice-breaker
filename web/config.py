import os


class Config:
    """
    This class represents the configuration and initialization of the local variable that are used by the application.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', f"{os.urandom(32)}")
    WTF_CSRF_ENABLED = True
