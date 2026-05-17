import os
from pathlib import Path
from dotenv import load_dotenv

basedir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=basedir / '.env')

class Config:
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '1234')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DB = os.getenv('MYSQL_DB', 'prueba_db')
    DATABASE_URL = os.getenv('DATABASE_URL')

    SQLALCHEMY_DATABASE_URI = DATABASE_URL or f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'static/uploads')
    PDF_FOLDER = os.getenv('PDF_FOLDER', 'static/uploads/pdfs')