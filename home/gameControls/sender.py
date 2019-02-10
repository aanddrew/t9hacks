# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

class Sender:
	def __init__(self, from_email, to_email):
		self.sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

		self.from_email = Email(from_email)
		self.to_email = Email(to_email)

		
	def send(self, subject, body):
		# subject = "output"
		content = Content("text/plain", body)
		mail = Mail(self.from_email, subject, self.to_email, content)

		response = self.sg.client.mail.send.post(request_body=mail.get())
		# print(response.status_code)
		# print(response.body)
		# print(response.headers)