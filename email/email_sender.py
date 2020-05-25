import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html_template = Path("d:\\OneDrive - SQLI\\Perso\\Code\\python\\email\\index.html")

html = Template(html_template.read_text())


email = EmailMessage()
email['from'] = "Juan Pablo CHACLAN"
email['to'] = 'jchaclan@gmail.com'
email['subject'] = 'Sent from Python'
name = "The name"

email.set_content(html.substitute({'name':name}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jchaclan.python@gmail.com','Robo2020Python')
    smtp.send_message(email)
    print('Great!')