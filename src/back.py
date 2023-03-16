import smtplib
import os
import mimetypes
from email import encoders
from email.mime.base import MIMEBase  
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio 
from aiogram.utils.helper import Helper, HelperMode, ListItem

class all_in_mail:
    Text = ""
    Subject = "Пересылка сообщения"
    Image=[]
    Audio=[]
    Forward_to = "user@mail"


    def send_mail(Message, Subject, Forward_to, Image, Audio):
        # create message object instance 
        msg = MIMEMultipart()
        message = Message

        Forward_to = "user@mail"

        login = "forward_sff@inbox.ru"
        password = "9NtSKsvrj7UjfcrHbafa"
        msg['From'] = "forward_sff@inbox.ru"
        msg['To'] = Forward_to  #  send_to
        msg['Subject'] = Subject
        # msg['Image'] = "Photos"

        # add in the message body 
        msg.attach(MIMEText(message, 'plain'))
        # msg.attach(MIMEImage(*Image))
        # msg.attach(MIMEAudio(*Audio))

        #create server 
        server = smtplib.SMTP_SSL('smtp.list.ru', 465)
        server.set_debuglevel(True)
        # server.starttls()

        # Login Credentials for sending the mail 
        server.login(login, password)

        # send the message via the server. 

        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return("Успешно отправлено на %s:" % (msg['To']))

    def clean():
        all_in_mail.Text = ""
        all_in_mail.Subject = "Пересылка сообщения"
        all_in_mail.Image=[]
        all_in_mail.Audio=[]
        all_in_mail.Forward_to = "user@mail"


class TestStates(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    TEST_STATE_1 = ListItem()
    TEST_STATE_2 = ListItem()
