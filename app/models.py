from app import db
from hashlib import md5
import urllib
import hashlib

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id) #python 2
		except NameError:
			return str(self.id) #python 3

	def avatar(self, size):
		return "http://www.gravatar.com/avatar/%s?s=%s" % (hashlib.md5(self.email.lower().encode('utf-8')).hexdigest(), size)

	def __repr(self):
		return '<User %r>' % (self.nickname)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr(self):
		return '<Post %r>' % (self.body)