import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from decouple import config


class Emails(object):
    def __init__(self):
        self.smtp_server = config('SMTP_SERVER')
        self.port = config('SMTP_PORT', cast=int)
        self.sender_email = config('SENDER_EMAIL')
        self.receiver_email = config('RECEIVER_EMAIL', cast=lambda x: x.split(','))
        self.subject = config('EMAIL_SUBJECT').replace('${PROJECT_NAME}', config('PROJECT_NAME'))
        with open(os.path.join(os.path.dirname(__file__), config('EMAIL_LOGO_FILE')), 'rb') as file:
            self.logo_img = file.read()
        with open(os.path.join(os.path.dirname(__file__), config('EMAIL_HTML_FILE')), 'r', encoding='UTF-8') as file:
            self.html = file.read().replace('${PROJECT_NAME}', config('PROJECT_NAME'))
        self.text = config('EMAIL_PLAIN_TEXT').replace('${PROJECT_NAME}', config('PROJECT_NAME'))

    def send_email(self, tests):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender_email
        message["To"] = ",".join(self.receiver_email)
        plain_part = MIMEText(self.text, "plain")
        message.attach(plain_part)
        html_part = MIMEMultipart("related")
        html_part.attach(MIMEText(self.html, "html"))
        logo_image = MIMEImage(self.logo_img)
        logo_image.add_header('Content-ID', '<logo>')
        html_part.attach(logo_image)
        message.attach(html_part)

        content = ''
        index = 1
        for test in tests:
            if test['screenshot'] != '':
                filename = f"{test['name']}.png"
                with open(test['screenshot'], "rb") as attachment:
                    screenshot = MIMEBase("application", "octet-stream")
                    screenshot.set_payload(attachment.read())
                encoders.encode_base64(screenshot)
                screenshot.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )
                message.attach(screenshot)

            sentence = ''
            if len(tests) != 1:
                sentence = f'{str(index)}\n'
            for key, value in test.items():
                sentence = f'{sentence}{key.upper()}: {value}\n'
            content = f'{content}\n{sentence}'
            index += 1

        details_log = MIMEText(f"Failed tests:\n{content}\n", "plain")
        details_log.add_header(
            "Content-Disposition",
            f"attachment; filename= details.log",
        )
        message.attach(details_log)

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.sendmail(from_addr=self.sender_email, to_addrs=self.receiver_email, msg=message.as_string())
