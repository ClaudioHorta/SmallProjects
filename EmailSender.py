import smtplib
from email.message import EmailMessage
from pathlib import Path # is similar to  os.path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = ' Sooru Hooru'
email['to'] = 'claudiohortahu@gmail.com'
email['subject'] = 'You won!'

email.set_content(html.substitute(name = 'TinTin'), 'html') # can add multiple variables as a dict

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('sooruhooru@gmail.com', 'ntte keox xcsg ognm')
	smtp.send_message(email)
	print('all good boos!')