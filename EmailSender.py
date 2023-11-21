import smtplib
from email.message import EmailMessage
from pathlib import Path  # pathlib is similar to os.path
from string import Template

# Read the content of the HTML template file using the Template class
html = Template(Path('index.html').read_text())

# Create an EmailMessage object
email = EmailMessage()
email['from'] = ' Sooru Hooru'
email['to'] = 'claudiohortahu@gmail.com'
email['subject'] = 'You won!'

# Set the content of the email using the HTML template with a substituted variable
email.set_content(html.substitute(name='TinTin'), 'html')  # Can add multiple variables as a dictionary

# Connect to the SMTP server and send the email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    
    # Login to the email account (replace 'the actual password' with the actual password)
    smtp.login('sooruhooru@gmail.com', 'the actual password')
    
    # Send the email message
    smtp.send_message(email)
    
    print('all good boos!')
