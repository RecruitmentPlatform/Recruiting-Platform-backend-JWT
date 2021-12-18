import os
from views.routes import app
from models.user import User

User.dbpath = "../frontend/db/db.sqlite"


if __name__ == "__main__":
    app.run()
