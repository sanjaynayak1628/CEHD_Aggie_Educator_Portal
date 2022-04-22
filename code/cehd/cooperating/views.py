"""
views file describing the APIs used in student time sheet API
"""
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


class CoopViews(APIView):
    """
    GET function to view the coop time sheets from the DB
    """

    def get(self, request, email, start_date=None, end_date=None, semester=None, status=None, year=None):
        """
        GET function implementation
        """
        print(f'{email}--{start_date}--{end_date}--{semester}--{status}--{year}')
        return render(request, f'cooperating/cooperatingview.html', status=status.HTTP_200_OK)


class CoopSubmit(APIView):
    """
    POST function to approve/reject the coop time sheets to the DB
    """

    def post(self, request, approve):
        print(approve)
        smtpHost = "smtp.gmail.com"
        smtpPort = 587
        mailUname = 'seprojtestemail@gmail.com'
        mailPwd = 'khwdhcmpdpkdrfmt'
        fromEmail = 'seprojtestemail@gmail.com'
        # mail body, recepients, attachment files
        # mailSubject = "test subject"
        # mailContentHtml = "Hi, Hope u are fine. <br/> This is a <b>test</b> mail from python script using an awesome library called <b>smtplib</b>"
        recepientsMailList = ["manisha1@tamu.edu", "maniii.dixit@gmail.com"]
        if approve == "true":
            # mail server parameters
            mailSubject = "Timesheet Approved"
            mailContentHtml = "Hi, Hope u are fine. <br/> This is a <b>test</b> mail from python script using an awesome library called <b>smtplib</b>"
        else:
            # mail server parameters
            mailSubject = "Timesheet Rejected"
            mailContentHtml = "Hi, Hope u are fine. <br/> This is a <b>test</b> mail from python script using an awesome library called <b>smtplib</b>"

            # attachmentFpaths = ["smtp.png", "poster.png"]
        sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
                  mailSubject, mailContentHtml, recepientsMailList)  # , attachmentFpaths)
        print("execution complete...")
        return render(request, f'cooperating/cooperatingview.html', status=status.HTTP_200_OK)


def sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail, mailSubject, mailContentHtml, recepientsMailList):
    # , attachmentFpaths):
    # create message object
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = ','.join(recepientsMailList)
    msg['Subject'] = mailSubject
    # msg.attach(MIMEText(mailContentText, 'plain'))
    msg.attach(MIMEText(mailContentHtml, 'html'))
    # create file attachments
    #     for aPath in attachmentFpaths:
    #         # check if file exists
    #         part = MIMEBase('application', "octet-stream")
    #         part.set_payload(open(aPath, "rb").read())
    #         encoders.encode_base64(part)
    #         part.add_header('Content-Disposition',
    #                         'attachment; filename="{0}"'.format(os.path.basename(aPath)))
    #         msg.attach(part)
    # Send message object as email using smptplib
    s = smtplib.SMTP(smtpHost, smtpPort)
    s.starttls()
    s.login(mailUname, mailPwd)
    msgText = msg.as_string()
    sendErrs = s.sendmail(fromEmail, recepientsMailList, msgText)
    s.quit()
    # check if errors occured and handle them accordingly
    if not len(sendErrs.keys()) == 0:
        raise Exception("Errors occurred while sending email", sendErrs)
