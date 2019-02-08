import smtplib
from email.message import EmailMessage
import logging

def send_email(emailSMTPHost,emailSMTPPort,emailSubject, emailFrom, emailTo, emailCC, emailBody):
    message = EmailMessage()
    message['Subject'] = emailSubject
    message['From'] = emailFrom
    message['To'] = emailTo
    message['CC'] = emailCC
    message.set_content(emailBody)
    print(message)
    
    try:
        logging.info("Sending email...")
        # Send the message via local SMTP server.
        mail_smtp_host = emailSMTPHost
        mail_smtp_port = emailSMTPPort
        with smtplib.SMTP(mail_smtp_host, mail_smtp_port) as email:
            email.send_message(message)
    except smtplib.SMTPException as e:
        logging.error("Could not send the email.\n {0}".format(e))