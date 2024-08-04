from email.message import EmailMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email import encoders
from email.mime.base import MIMEBase

from app import app
from app.utils.logging import get_logger
logger = get_logger()

def send_mail(recipient,subject,body):
    '''
    明文 普通 text 文字发送
    '''
    logger.info("send mail now ******* ")
    sender = app.config['MAIL_SENDER']
    recipient = "zhongaibiancheng@outlook.com"
    message = body

    logger.info("send mail body ******* %s"%(body))
    
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject

    logger.info("send mail Subject ******* %s"%(subject))

    email.set_content(message)
    try:
        # initialize connection to our email server, we will use Outlook here
        smtp = smtplib.SMTP('smtp-mail.outlook.com', port='587')
        smtp.ehlo()  # send the extended hello to our server
        smtp.starttls()  # tell server we want to communicate with TLS encryption
        smtp.login(sender, "Admin@2402")
        logger.info("smtp login *******")
        smtp.sendmail(sender, recipient, email.as_string())
        logger.info("smtp send mail finished *******")
              
        smtp.quit()  # finally, don't forget to close the connection
    except (Exception) as error:
            logger.error(error)
            raise error 

def send_mail_with_html(recipient):
    '''
    html发送内容
    '''
    logger.info("send mail now ******* ")
    sender = app.config['MAIL_SENDER']
    recipient = "zhongaibiancheng@outlook.com"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender
    message["To"] = recipient

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a> 
        has many great tutorials.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    try:
        # initialize connection to our email server, we will use Outlook here
        smtp = smtplib.SMTP('smtp-mail.outlook.com', port='587')
        smtp.ehlo()  # send the extended hello to our server
        smtp.starttls()  # tell server we want to communicate with TLS encryption
        smtp.login(sender, "Admin@2402")
        logger.info("smtp login *******")
        smtp.sendmail(sender, recipient, message.as_string())
        logger.info("smtp send mail finished *******")
              
        smtp.quit()  # finally, don't forget to close the connection
    except (Exception) as error:
            logger.error(error)
            raise error 


def send_mail_with_attachment(recipient):
    '''
    添加附件发送
    '''
    logger.info("send mail now ******* ")
    sender = app.config['MAIL_SENDER']
    recipient = "zhongaibiancheng@outlook.com"
    body = "This is an email with attachment sent from Python"

    message = MIMEMultipart("alternative")
    message["Subject"] = "attachement test"
    message["From"] = sender
    message["To"] = recipient

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "/Users/lichenggang/workspace/PrayaInstitue/Server/data/2.png"

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    try:
        smtp = smtplib.SMTP('smtp-mail.outlook.com', port='587')
        smtp.ehlo()  # send the extended hello to our server
        smtp.starttls()  # tell server we want to communicate with TLS encryption
        smtp.login(sender, "Admin@2402")
        logger.info("smtp login *******")
        smtp.sendmail(sender, recipient, message.as_string())
        logger.info("smtp send mail finished *******")
              
        smtp.quit()  # finally, don't forget to close the connection
    except (Exception) as error:
            logger.error(error)
            raise error 