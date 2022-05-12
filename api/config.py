import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

# POSTGRES_USER = os.environ.get("POSTGRES_USER")
# POSTGRES_PW = os.environ.get("POSTGRES_PW")
# POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
# POSTGRES_DB = os.environ.get("POSTGRES_DB")

# DB_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_HOST}/{POSTGRES_DB}"
DB_URL = os.environ["DATABASE_URL"]


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "abc"
    SQLALCHEMY_DATABASE_URI = DB_URL or f"psql:///{os.path.join(basedir)}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
