# ─────────────────────────────────────────────
# PART 2: Composition version
# Each channel is its own small class
# Notification just uses them — it doesn't inherit
# ─────────────────────────────────────────────
from typing import Any


class EmailChannel:
    def send(self, message: str):
        print(f"📧 Email sent: {message}")


class SMSChannel:
    def send(self, message: str):
        print(f"📱 SMS sent: {message}")


class PushChannel:
    def send(self, message: str):
        print(f"🔔 Push sent: {message}")


class Notification:
    def __init__(self, channels: Any):
        self.channels = channels  # receives a LIST of channel objects

    def send(self, message: str):
        for channel in self.channels:
            channel.send(message)  # delegates the work to each channel


# Send via Email only:
n = Notification(channels=[EmailChannel()])
n.send("Your order is confirmed!")
# 📧 Email sent: Your order is confirmed!

# Send via Email + SMS:
n = Notification(channels=[EmailChannel(), SMSChannel()])
n.send("Your order is confirmed!")
# 📧 Email sent: Your order is confirmed!
# 📱 SMS sent: Your order is confirmed!

# Send via all three:
n = Notification(channels=[EmailChannel(), SMSChannel(), PushChannel()])
n.send("Your order is confirmed!")
# 📧 Email sent: Your order is confirmed!
# 📱 SMS sent: Your order is confirmed!
# 🔔 Push sent: Your order is confirmed!

# ─────────────────────────────────────────────
# PART 3: Adding WhatsApp — the real proof
# Inheritance: 8 new classes
# Composition: exactly 1 new class
# ─────────────────────────────────────────────


class WhatsAppChannel:
    def send(self, message):
        print(f"💬 WhatsApp sent: {message}")


# That's it. Now use it anywhere:
n = Notification(channels=[EmailChannel(), WhatsAppChannel()])
n.send("Your package has shipped!")
# 📧 Email sent: Your package has shipped!
# 💬 WhatsApp sent: Your package has shipped!

n = Notification(channels=[SMSChannel(), PushChannel(), WhatsAppChannel()])
n.send("Flash sale starts now!")
# 📱 SMS sent: Flash sale starts now!
# 🔔 Push sent: Flash sale starts now!
# 💬 WhatsApp sent: Flash sale starts now!

# Notification class never changed.
# Zero new combinations needed.
# Just plug in the new channel and go.
