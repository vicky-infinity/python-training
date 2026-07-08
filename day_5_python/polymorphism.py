# Parent Class
# This acts as a common blueprint for all notification types

class Notification:

    def __init__(self, receiver):
        self.receiver = receiver

    def send(self, message):
        return f"Sending notification to {self.receiver}: {message}"


# Email Notification
# Inherits from Notification
# Overrides send() method

class EmailNotification(Notification):

    def send(self, message):
        return f"Email sent to {self.receiver}: {message}"


# SMS Notification
# Inherits from Notification
# Overrides send() method

class SMSNotification(Notification):

    def send(self, message):
        return f"SMS sent to {self.receiver}: {message}"


# WhatsApp Notification
# Inherits from Notification
# Overrides send() method

class WhatsAppNotification(Notification):

    def send(self, message):
        return f"WhatsApp message sent to {self.receiver}: {message}"


# -----------------------------------------
# Creating Objects
# -----------------------------------------

email = EmailNotification("vicky@gmail.com")

sms = SMSNotification("9876543210")

whatsapp = WhatsAppNotification("9876543210")


# -----------------------------------------
# Polymorphism
# Same method name -> send()
# Different behavior based on object type
# -----------------------------------------

notifications = [email, sms, whatsapp]

for notification in notifications:

    result = notification.send("Your order has been placed successfully")

    print(result)

    