import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_HOST = os.environ["DB_HOST"]
DB_HOST_PORT = os.environ["DB_HOST_PORT"]
DB_NAME = os.environ["DB_NAME"]


BACKEND_HOST = os.environ["BACKEND_HOST"]
BACKEND_PORT = int(os.environ["BACKEND_PORT"])
BACKEND_AUTH_SECRET_KEY = os.environ["BACKEND_AUTH_SECRET_KEY"]
BACKEND_USER_MANAGER_SECRET_KEY = os.environ["BACKEND_USER_MANAGER_SECRET_KEY"]

CACHE_HOST = os.environ["CACHE_HOST"]
CACHE_HOST_PORT = int(os.environ["CACHE_HOST_PORT"])
CACHE_PASS = os.environ["CACHE_PASS"]

MAIL_SERVICE_EMAIL = os.environ["MAIL_SERVICE_EMAIL"]
MAIL_SERVICE_PASS = os.environ["MAIL_SERVICE_PASS"]
MAIL_SERVICE_SMTP_SERVER = os.environ["MAIL_SERVICE_SMTP_SERVER"]
MAIL_SERVICE_TOKEN_EXPIRATION_TIME = int(os.environ["MAIL_SERVICE_TOKEN_EXPIRATION_TIME"])

FRONTEND_ORIGIN = os.environ["FRONTEND_ORIGIN"]