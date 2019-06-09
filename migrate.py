"""
https://flask-migrate.readthedocs.io/en/latest/
migrates/updates the database whenever schemas, columns, etc. change. summary of steps to follow from the CLI:

1. set the FLASK_APP environment variable first before migrating
export FLASK_APP=migrate.py

2. initialize the database (will only need to do this once):
flask db init

3. migrate the db:
flask db migrate

4. apply migration to the db:
flask db upgrade

repeat steps 3 and 4 each time the models change
"""

from flask_migrate import Migrate
from model import db
from run import create_app

app = create_app('config')
migrate = Migrate(app, db, compare_type=True)
