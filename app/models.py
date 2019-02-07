from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    citations = db.relationship('Citation', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    body = db.Column(db.String(140))
#    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#    def __repr__(self):
#        return '<Post {}>'.format(self.body)

class Citation(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    SRR = db.Column(db.Integer)
    TRT = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #looks like relationship respect la CASSE (H with History)
    histories = db.relationship('History', backref='citation', lazy='dynamic')

    def __repr__(self):
        return '<Citation {} (text={}, SRR={}, TRT={})>'.format(
                self.number, self.text[:5], self.SRR, self.TRT)

class History(db.Model):
    number=db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    SRR = db.Column(db.Integer)
    TRT = db.Column(db.Float)
    #looks like ForeignKey don't respect la CASSE (no C in citation)
    citation_id = db.Column(db.Integer, db.ForeignKey('citation.number'))

    def __repr__(self):
        return '<History {} (timestamp={}, SRR={}, TRT={}, citation_id={})>'.format(
                self.number, self.timestamp, self.SRR, self.TRT, self.citation_id)