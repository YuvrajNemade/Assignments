import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.schemas.inventory_schemas import Email
from scripts.constant.email_constant import email_object
from scripts.utils.mongo_utility import Item_handler
from scripts.logging.logs import logger


class Email_handler:
    """this class helps in building an smtp mail structure for sending to the recepient"""

    def send_email(self, email: Email):
        sender_email = email_object.email_name
        sender_password = email_object.email_password
        receiver_email = email.rec_email

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Total Price Of The Inventory List"

        price_object = Item_handler()

        body = price_object.find_total()
        body = str(body)
        message.attach(MIMEText(("Total amount : " + body), "plain"))

        try:

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            server.quit()
            logger.info({"message": "Email sent successfully"})

        except Exception as e:
            logger.error({"message": str(e)})
            return {"message": str(e)}

