import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

POSTGRES_USER = os.environ.get("USER")
POSTGRES_PW = os.environ.get("PASSWORD")
POSTGRES_HOST = os.environ.get("HOST")
POSTGRES_DB = os.environ.get("DATABASE")
POSTGRES_PORT = os.environ.get("PORT")

# DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
# DB_URL = os.environ["DATABASE_URL"].replace("postgres://", "postgresql://", 1)
DB_URL = "postgresql://habitat_user:Ie1zqUIPT2L6znhTFgxpOiZgDV0ewSjT@dpg-cba13b4objdalo36h6qg-a.frankfurt-postgres.render.com/habitat"


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "abc"
    SQLALCHEMY_DATABASE_URI = DB_URL or f"psql:///{os.path.join(basedir)}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
