import os
from configparser import ConfigParser


def config(filename='TravelLogger.ini', section='DB_ACCESS'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to DB_ACCESS
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


db_credentials = config()
username = db_credentials['user']
database = db_credentials['database']
host = db_credentials['host']
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgresql://{}@{}/{}'.format(username, host, database)
