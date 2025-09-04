from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# flask shell

# >>> db.create_all()
# >>> db.session
# <sqlalchemy.orm.scoping.scoped_session object at 0x000002447A5AD2B0>
# >>> db.session.commit()
# >>> exit()

# user = User(username="admin",password="123")
#user.username
#db.session.add(user)
#db.session.commit()
#db.exit()