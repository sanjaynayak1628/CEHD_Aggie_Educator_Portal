"""
Utility files common for all apps
"""
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()

SMTP_HOST = str(os.getenv('SMTP_HOST'))
SMTP_PORT = int(os.getenv('SMTP_PORT'))
MAIL_USERNAME = str(os.getenv('MAIL_USERNAME'))
MAIL_PASSWORD = str(os.getenv('MAIL_PASSWORD'))
FROM_EMAIL = str(os.getenv('FROM_EMAIL'))
RECIPIENTS_MAIL_LIST_APPROVE = json.loads(os.getenv('RECIPIENTS_MAIL_LIST_APPROVE'))
RECIPIENTS_MAIL_LIST_REJECT = json.loads(os.getenv('RECIPIENTS_MAIL_LIST_REJECT'))
RECIPIENTS_MAIL_LIST_SUBMIT = json.loads(os.getenv('RECIPIENTS_MAIL_LIST_SUBMIT'))


def send_email(mail_subject, mail_content_html, recipients_mail_list):
    """
    Helper function to send the email as per the recipients
    """
    # create message object
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = ','.join(recipients_mail_list)
    msg['Subject'] = mail_subject
    msg.attach(MIMEText(mail_content_html, 'html'))
    s = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    s.starttls()
    s.login(MAIL_USERNAME, MAIL_PASSWORD)
    msg_text = msg.as_string()
    send_errs = s.sendmail(FROM_EMAIL, recipients_mail_list, msg_text)
    s.quit()
    # check if errors occurred and handle them accordingly
    if not len(send_errs.keys()) == 0:
        raise Exception("Errors occurred while sending email", send_errs)


def timesheet_approve():
    """
    Send email to student if time sheets are approved by the cooperating teacher
    """
    # mail server parameters
    mail_subject = "Timesheet Approved"
    recipients_mail_list = RECIPIENTS_MAIL_LIST_APPROVE
    mail_content_html = "Hi, Hope u are fine. <br/> This is a <b>test</b> mail from python script using an " \
                        "awesome library called <b>smtplib</b> "
    send_email(mail_subject, mail_content_html, recipients_mail_list)


def timesheet_reject():
    """
    Send email to student if time sheets are rejected by the cooperating teacher
    """
    # mail server parameters
    mail_subject = "Timesheet Rejected"
    recipients_mail_list = RECIPIENTS_MAIL_LIST_REJECT
    mail_content_html = "Hi, Hope u are fine. <br/> This is a <b>test</b> mail from python script using an " \
                        "awesome library called <b>smtplib</b> "
    send_email(mail_subject, mail_content_html, recipients_mail_list)


def timesheet_submit():
    """
    Send email to cooperating teacher if time sheets are submitted by the student
    """
    # mail server parameters
    # print("Inside timesheet submit email")
    mail_subject = "Timesheet Submitted"
    recipients_mail_list = RECIPIENTS_MAIL_LIST_SUBMIT
    mail_content_html = "Hi, Hope u are fine. <br/> This is a <b>test</b> mail from python script using an " \
                        "awesome library called <b>smtplib</b> "
    send_email(mail_subject, mail_content_html, recipients_mail_list)
