from database import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    # id (int), username (text), password (text)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True) # NOT NULL
    password = db.Column(db.String(80), nullable=False)





# flask shell

# >>> db.create_all()
# >>> db.session
# <sqlalchemy.orm.scoping.scoped_session object at 0x000002447A5AD2B0>
# >>> db.session.commit()
# >>> exit()