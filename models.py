from app import db

class User(db.Document):
  username = db.StringField(default=Teue)
	password = db.StringField(default=True)
  email = db.EmailField(unique=True)
