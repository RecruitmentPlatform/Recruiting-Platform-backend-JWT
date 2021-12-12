import os
from views.routes import app
from models.user import User

PATH = os.path.dirname(__file__)
User.dbpath = os.path.join(PATH, "data", "db.sqlite")


if __name__ == "__main__":
    app.run()
