from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id=db.Column(db.Integer,index=True,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100))
    uname=db.Column(db.String(100))
    email=db.Column(db.String(100),unique=True)
    phone=db.Column(db.String,nullable=True)
    password=db.Column(db.String,unique=True)
    image=db.Column(db.String,unique=True,nullable=True)
    bio=db.Column(db.String)
    code=db.Column(db.Integer,unique=True,nullable=False)
    confirmed=db.Column(db.Integer,default=0)

    def save(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()

    def __init__(self):
        return

    def encrypt_password(self,plaintext_password):

        if plaintext_password:
            self.password = generate_password_hash(plaintext_password)
        return

    def authenticate(self,hash,passw):
        x=check_password_hash(hash, passw)
        return x

    def update(self):
        db.session.commit()