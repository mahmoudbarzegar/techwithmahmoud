# ─────────────────────────────────────────────
# THE PROBLEM: client wants Email + SMS together
# We have to create a NEW class for every combination
# ─────────────────────────────────────────────


class Notification:
    def __init__(self, message: str):
        self.message = message

    def send(self) -> None:
        raise NotImplementedError


class EmailAndSMSNotification(Notification):
    def send(self) -> None:
        print(f"📧 Email sent: {self.message}")
        print(f"📱 SMS sent: {self.message}")


class EmailAndPushNotification(Notification):
    def send(self) -> None:
        print(f"📧 Email sent: {self.message}")
        print(f"🔔 Push sent: {self.message}")


class SMSAndPushNotification(Notification):
    def send(self) -> None:
        print(f"📱 SMS sent: {self.message}")
        print(f"🔔 Push sent: {self.message}")


class EmailAndSMSAndPushNotification(Notification):
    def send(self) -> None:
        print(f"📧 Email sent: {self.message}")
        print(f"📱 SMS sent: {self.message}")
        print(f"🔔 Push sent: {self.message}")


# Already 7 classes for just 3 channels.
# Now the client says: "Can we add WhatsApp too?"

# New classes needed:
#   WhatsAppNotification
#   EmailAndWhatsAppNotification
#   SMSAndWhatsAppNotification
#   PushAndWhatsAppNotification
#   EmailAndSMSAndWhatsAppNotification
#   EmailAndPushAndWhatsAppNotification
#   SMSAndPushAndWhatsAppNotification
#   EmailAndSMSAndPushAndWhatsAppNotification

# 4 channels → 15 classes total
# 5 channels → 31 classes total
# This is called the "class explosion" problem.
