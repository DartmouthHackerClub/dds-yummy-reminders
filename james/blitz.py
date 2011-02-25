# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

me = "Hacktown <james.a.murdza@dartmouth.edu>"
you = "james.a.murdza@dartmouth.edu"
msg = MIMEText("hello!")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = "hi there!"
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP()
s.connect()
s.sendmail(me, [you], msg.as_string())
s.quit()