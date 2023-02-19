import smtplib
import ssl
import os

PASSWORD = os.getenv('50days_python_pass')


def email_sender(user, to, content):
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as email:
        email.login(user=user, password=PASSWORD, initial_response_ok=True)
        email.sendmail(from_addr=user, to_addrs=to, msg=content)





