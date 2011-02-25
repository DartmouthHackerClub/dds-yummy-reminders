# INTENSE BLITZING ACTION BY JAMES

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

def blitz(address, subject, text):

	me = "Hacktown <james.a.murdza@dartmouth.edu>"
	you = address
	msg = MIMEText(text)

	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = subject
	msg['From'] = me
	msg['To'] = you

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP()
	s.connect()
	s.sendmail(me, [you], msg.as_string())
	s.quit()