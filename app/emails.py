from flask.ext.mail import Message
from app import mail
from flask import render_template
from config import ADMINS

def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender = ADMINS[0], recipients = recipients)
	msg.body = text_body
	msg.html = html_body
	mail.send(msg)

def follower_notification(followed, follower):
	print("--> %s Sending email" % follower.nickname)
	send_email("[microblog] %s is now following you!" % follower.nickname,
				ADMINS[0],
				[followed.email],
				render_template("follower_email.txt",
					user = followed, follower = follower),
				render_template("follower_email.html",
					user = followed, follower = follower))
