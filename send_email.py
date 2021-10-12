import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from decouple import config

SENDER_EMAIL = config('SENDER_EMAIL')
PASSWORD = config('PASSWORD')
RECEIVER_EMAIL = config('RECEIVER_EMAIL')
SMTP_SERVER = config('SMTP_SERVER')
PORT = config('PORT')


def send_email(message=None, subject=None, picture=None, bcc=None, receiver_email=RECEIVER_EMAIL):

	msg = MIMEMultipart()

	msg['From'] = SMTP_SERVER
	msg['To'] = RECEIVER_EMAIL

	if bcc:
		msg['Bcc'] = bcc

	if subject:
		msg['Subject'] = subject

	if picture:

		with open(picture, 'rb') as fp:
			msgImage = MIMEImage(fp.read())
		msgImage.add_header('Content-ID', '<image1>')
		msg.attach(msgImage)

	if message:
		msg.attach(MIMEText(message, 'plain', 'utf-8'))
	
	if not message and not picture and not subject and not bcc:
		print("There was no input for the entry!!")
		quit()

	server = smtplib.SMTP(SMTP_SERVER, PORT)
	server.starttls()
	# server.set_debuglevel(1)
	server.login(SENDER_EMAIL, PASSWORD)
	text = msg.as_string()
	server.sendmail(SENDER_EMAIL, receiver_email, text)
	server.quit()
