# ─────────────────────────────────────────────
# PART 1: Inheritance version
# Looks fine at first... but watch what happens
# ─────────────────────────────────────────────


class Notification:
    def __init__(self, message: str):
        self.message = message

    def send(self) -> None:
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self) -> None:
        print(f"📧 Email sent: {self.message}")


class SMSNotification(Notification):
    def send(self) -> None:
        print(f"📱 SMS sent: {self.message}")


class PushNotification(Notification):
    def send(self) -> None:
        print(f"🔔 Push sent: {self.message}")


# Looks clean so far. Let's use it:
email = EmailNotification("Your order is confirmed!")
email.send()  # 📧 Email sent: Your order is confirmed!

sms = SMSNotification("Your order is confirmed!")
sms.send()  # 📱 SMS sent: Your order is confirmed!
