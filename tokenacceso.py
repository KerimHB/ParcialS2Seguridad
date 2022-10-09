import random
import smtplib
from llaves import *

otp = random.randint(1000,10000)
print(otp)

sent_from = 'developermodebv@gmail.com'
to = 'kerimhernandez9@gmail.com'
subject = 'Token de Acceso'
body = "El token generado es: "+str(otp)+"\n\n- Token de Acceso"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!') 
except:
    print ('Something went wrong...')