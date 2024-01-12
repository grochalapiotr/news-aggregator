import ssl
import json
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from news_aggregator.utils.credentials import EMAIL, PASSWORD


class Mail_Handler:

    def __init__(self) -> None:
        self.body = ""
        self.bbc_news = ""
        self.vox_news = ""
        self.pcgamer_news = ""
        
    def send_email(self, mail_receiver):

        with open(f'articles/bbc-{datetime.datetime.now().date()}.json') as f:
            bbc = json.load(f)
        with open(f'articles/vox-{datetime.datetime.now().date()}.json') as f:
            vox = json.load(f)
        with open(f'articles/pcgamer-{datetime.datetime.now().date()}.json') as f:
            pcgamer = json.load(f)

        

        for article in bbc:
            self.bbc_news += f"""
            <div class="news">
                <h3>{article['title']}</h3>
                <h4>BBC</h4>
                <h5>Article tone: {article['sentiment']}</h5>
                <p>{article['summary']}</p>
                <a href="{article['url']}" class="read-more-btn">Read More</a>
            </div>"""

        for article in pcgamer:
            self.pcgamer_news += f"""
            <div class="news">
                <h3>{article['title']}</h3>
                <h4>PC GAMER</h4>
                <h5>Article tone: {article['sentiment']}</h5>
                <p>{article['summary']}</p>
                <a href="{article['url']}" class="read-more-btn">Read More</a>
            </div>"""

        for article in vox:
            self.vox_news += f"""
            <div class="news">
                <h3>{article['title']}</h3>
                <h4>VOX</h4>
                <h5>Article tone: {article['sentiment']}</h5>
                <p>{article['summary']}</p>
                <a href="{article['url']}" class="read-more-btn">Read More</a>
            </div>"""


        self.body = """
<html>
  <head>
    <style>
      body {
        font-family: 'baskerville', sans-serif;
        color: black;
      }

      h1 {
        text-align: center;
        font-weight: bold;
      }

      .news-container {
        display: flex;
        justify-content: space-between;
      }

      .news-column {
        width: 48%; 
      }

      .news {
        background-color: #fff8e1; 
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 10px; 
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); 
      }

      .read-more-btn {
        background-color: #bc6c25;
        color: #fff;
        padding: 8px 20px; 
        text-decoration: none;
        display: inline-block;
        border-radius: 20px; 
        margin-top: 8px;
        text-align: center;
      }
      .news p {
        text-align: justify;
      }
    </style>
  </head>
  <body>
    <h1>📰 DAILY NEWS - """+str(datetime.datetime.now().date())+""" 📰</h1>
    <div class="news-container">
      <div class="news-column">
"""+self.bbc_news+self.pcgamer_news+"""
      </div>
      <div class="news-column">
"""+self.vox_news+"""
      </div>
    </div>
  </body>
</html>

"""


        em = MIMEMultipart()
        em['From'] = EMAIL
        em['TO'] = mail_receiver
        em['Subject'] = "Daily News - " + str(datetime.datetime.now().date())
        em.attach(MIMEText(self.body, 'html'))

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.sendmail(EMAIL, mail_receiver, em.as_string())
