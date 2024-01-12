import ssl
import json
import smtplib
import datetime
from news_aggregator.utils.credentials import EMAIL, PASSWORD

from email.message import EmailMessage


class Mail_Handler:

    def __init__(self) -> None:
        self.body = ""
        
    def send_email(self, mail_receiver):

        with open(f'articles/bbc-{datetime.datetime.now().date()}.json') as f:
            bbc = json.load(f)

        for article in bbc:
            self.body += article['title'] + "\n\n" + article['summary'] + f"\nRead more: {article['url']}"+"\n\n\n\n\n"


        em = EmailMessage()
        em['From'] = EMAIL
        em['TO'] = mail_receiver
        em['Subject'] = "Daily News"
        em.set_content(self.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.sendmail(EMAIL, mail_receiver, em.as_string())
