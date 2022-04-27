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


def timesheet_approve(coop_name, approve_date, start_date, end_date):
    """
    Send email to student if time sheets are approved by the cooperating teacher
    """
    # mail server parameters
    mail_subject = "Timesheet Approved"
    recipients_mail_list = RECIPIENTS_MAIL_LIST_APPROVE
    mail_content_html = "Hi, <br/>The timesheets submitted for the dates between {} and {} have been approved on {} " \
                        "by {}.<br/>You can login to your account to verify the status of your submitted time sheets." \
                        "<br/><br/>Best regards"\
        .format(start_date, end_date, approve_date, coop_name)
    send_email(mail_subject, mail_content_html, recipients_mail_list)


def timesheet_reject(coop_name, coop_email, rejection_date, start_date, end_date):
    """
    Send email to student if time sheets are rejected by the cooperating teacher
    """
    # mail server parameters
    mail_subject = "Timesheet Rejected | Contact your assigned cooperating teacher"
    recipients_mail_list = RECIPIENTS_MAIL_LIST_REJECT
    mail_content_html = "Hi, <br/>The timesheets submitted for the dates between {} and {} have been rejected on {} " \
                        "by {}.<br/>Please contact your assigned cooperating teacher, {} ({}) for more information. " \
                        "<br/><br/>Best regards"\
        .format(start_date, end_date, rejection_date, coop_name, coop_name, coop_email)
    send_email(mail_subject, mail_content_html, recipients_mail_list)


def timesheet_submit(student_name, student_email, submission_date):
    """
    Send email to cooperating teacher if time sheets are submitted by the student
    """
    # mail server parameters
    # print("Inside timesheet submit email")
    mail_subject = "Timesheet Submitted | Waiting for approval"
    recipients_mail_list = RECIPIENTS_MAIL_LIST_SUBMIT
    mail_content_html = "Hi, <br/>The student <b>{} ,{}</b> has submitted the timesheet on <b>{}</b> for approval. " \
                        "Please login to your account to approve the time sheets.<br/><br/>Best regards"\
        .format(student_name, student_email, submission_date)
    send_email(mail_subject, mail_content_html, recipients_mail_list)
