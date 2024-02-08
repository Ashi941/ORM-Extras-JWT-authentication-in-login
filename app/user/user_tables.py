from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(80), unique =False, nullable = False)
    password = db.Column(db.String(80), unique =True, nullable = False)
    email = db.Column(db.String(20),unique =True, nullable = False)
    mobile = db.Column(db.Text(120),unique =False, nullable = False )
    city = db.Column(db.String(12), unique =False, nullable = True)
    designation = db.Column(db.String(12), unique =False, nullable = True)