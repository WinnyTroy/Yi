from app import db

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, unique=False)
    lname = db.Column(db.String, unique=False)
    email = db.Column(db.String(120), unique=True)
    data_of_birth = db.Column(db.datetime, unique=False)
    location = db.Column(db.String, nullable=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email