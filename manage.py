# manage.py

import sys

import isort
from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

isort.file("manage.py")

app = create_app()
cli = FlaskGroup(app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(username="michael", email="hermanmu@gmail.com"))
    db.session.add(User(username="michaelherman", email="michael@mherman.org"))
    db.session.commit()


if __name__ == "__main__":
    cli()