from flask_script import Manager, prompt_bool, Command

from app import db
from app.models import Category, Product, User

manager = Manager(usage="Perform database operations")


@manager.command
def createdb():
    db.create_all()


@manager.command
def drop():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()


@manager.command
def recreate():
    if prompt_bool(
            "Are you sure you want to rebuild your database"):
        db.drop_all()


@manager.command
def init_data():
    user = User(username="Test", email="test@mail.com", password_hash="password")
    db.session.add(user)
    p = Category(name="test post")
    db.session.add(p)
    u = Product(name="Test", price="122", count="122", kind="122",author = p)
    db.session.add(u)
    db.session.commit()
    print("Initialization completed")