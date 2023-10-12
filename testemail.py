import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'your_email@example.com'
password = 'your_password'

smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()

smtp_connection.login(username, password)

from_email = username
to_email = 'zubair.anwar@cdph.ca.gov'
subject = 'Test Email'
message = 'This is a test email sent from Python.'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

smtp_connection.sendmail(from_email, to_email, msg.as_string())
smtp_connection.quit()
