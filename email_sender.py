import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Khan Mehedee'
email['to'] = 'khan@zerotomastery.io'
email['subject'] = 'you won 1,000,000 dollars!'

email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zerotomastery1@gmail.com', 'helloztmmyoldfriend1')
    smtp.send_message(email)
    print('all good')