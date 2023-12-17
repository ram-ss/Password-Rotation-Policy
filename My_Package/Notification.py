import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Notification:
    """
    Notification class for sending emails using SMTP.

    Attributes:
    - __username (str): The username used for authentication.
    - __password (str): The password used for authentication.

    Methods:
    - __init__(username: str, password: str):
        Initializes a Notification instance.

    - getUsername() -> str:
        Returns the username used for authentication.

    - getPassword() -> str:
        Returns the password used for authentication.

    - composeMessage(details: dict) -> str:
        Composes an email message based on the provided details.
        Parameters:
            - details (dict): A dictionary containing email details, including "To", "Subject", and "Message".
        Returns:
            - str: The composed email message as a string.

    - sendEmail(recipient: list):
        Sends emails to the specified recipients based on the provided details.
        Parameters:
            - recipient (list): A list of dictionaries, each containing details for a recipient, including "To", "Subject", and "Message".
    """

    def __init__(self, username: str, password: str):
        """
        Initializes a Notification instance with the provided username and password.
        
        Parameters:
            - username (str): The username used for authentication.
            - password (str): The password used for authentication.
        """
        self.__username = username
        self.__password = password

    def getUsername(self) -> str:
        """
        Returns the username used for authentication.

        Returns:
            - str: The username.
        """
        return self.__username
    
    def getPassword(self) -> str:
        """
        Returns the password used for authentication.

        Returns:
            - str: The password.
        """
        return self.__password
    
    def composeMessage(self, details: dict) -> str:
        """
        Composes an email message based on the provided details.

        Parameters:
            - details (dict): A dictionary containing email details, including "To", "Subject", and "Message".

        Returns:
            - str: The composed email message as a string.
        """
        msg = MIMEMultipart()
        msg["From"] = self.getUsername()
        msg["To"] = details["To"]
        msg["Subject"] = details["Subject"]
        msg.attach(MIMEText(details["Message"]))
        return msg.as_string()

    def sendEmail(self, recipient: list):
        """
        Sends emails to the specified recipients based on the provided details.

        Parameters:
            - recipient (list): A list of dictionaries, each containing details for a recipient, including "To", "Subject", and "Message".
        """
        port = 587  # Official default port for SMTP
        mailServer = smtplib.SMTP("smtp.gmail.com", port)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self.getUsername(), self.getPassword())
        mailServer.sendmail(self.getUsername(), recipient["To"], self.composeMessage(recipient))
        mailServer.quit()
