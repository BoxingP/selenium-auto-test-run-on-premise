import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from decouple import config


class Emails(object):
    def __init__(self):
        self.smtp_server = config('SMTP_SERVER')
        self.port = config('SMTP_PORT', cast=int)
        self.sender_email = config('SENDER_EMAIL')
        self.receiver_email = config('RECEIVER_EMAIL', cast=lambda x: x.split(','))
        self.subject = config('EMAIL_SUBJECT')
        self.text = config('EMAIL_TEXT').encode().decode('unicode_escape')

    def send_email(self, tests):
        message = MIMEMultipart()
        message["Subject"] = self.subject
        message["From"] = self.sender_email
        message["To"] = ",".join(self.receiver_email)
        part = MIMEText(self.text, "plain")
        message.attach(part)
        content = ''
        index = 1
        for test in tests:
            filename = f"{test['name']}.png"
            with open(test['screenshot'], "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            message.attach(part)

            sentence = ''
            if len(tests) != 1:
                sentence = str(index) + '\n'
            for key, value in test.items():
                sentence = sentence + '%s: %s\n' % (key.upper(), value)
            content = content + '\n%s' % sentence
            index += 1

        part = MIMEText(f"Failed tests:\n{content}\n", "plain")
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= details.log",
        )
        message.attach(part)

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.sendmail(from_addr=self.sender_email, to_addrs=self.receiver_email, msg=message.as_string())
