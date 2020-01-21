import pymysql

# from flask import current_app, g
from flask.cli import with_appcontext
from flaskps.config import Config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy


# Configuración sqlalchemy

def get_engine():
    url = 'mysql+pymysql://%s:%s@%s/%s' % (Config.DB_USER, Config.DB_PASS, Config.DB_HOST, Config.DB_NAME)
    engine = create_engine(url)
    return engine


def get_session():
    Base.metadata.bind = Engine
    DBSession = sessionmaker(bind=Engine)
    return DBSession()


Engine = get_engine()
Base = declarative_base(Engine)
db = SQLAlchemy()
Session = get_session()
