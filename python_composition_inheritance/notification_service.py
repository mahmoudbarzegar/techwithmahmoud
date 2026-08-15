# ─────────────────────────────────────────────
# PART 4: Runtime flexibility
# Composition lets you change behavior while the program is running
# Inheritance cannot do this — the class is fixed at definition time
# ─────────────────────────────────────────────
from typing import Any


class EmailChannel:
    def send(self, message: str) -> None:
        print(f"📧 Email sent: {message}")


class SMSChannel:
    def send(self, message: str) -> None:
        print(f"📱 SMS sent: {message}")


class WhatsAppChannel:
    def send(self, message: str) -> None:
        print(f"💬 WhatsApp sent: {message}")


class NotificationService:
    def __init__(self):
        self.channels = []

    def add_channel(self, channel: Any) -> None:
        self.channels.append(channel)
        print(f"✅ {channel.__class__.__name__} added")

    def remove_channel(self, channel_type: Any) -> None:
        self.channels = [c for c in self.channels if not isinstance(c, channel_type)]
        print(f"🗑️  {channel_type.__name__} removed")

    def send(self, message: str) -> None:
        if not self.channels:
            print("⚠️  No channels configured!")
            return
        for channel in self.channels:
            channel.send(message)


service = NotificationService()

service.add_channel(EmailChannel())  # ✅ EmailChannel added
service.add_channel(SMSChannel())  # ✅ SMSChannel added
service.send("Hello!")
# 📧 Email sent: Hello!
# 📱 SMS sent: Hello!

# User disables SMS notifications:
service.remove_channel(SMSChannel)  # 🗑️  SMSChannel removed
service.add_channel(WhatsAppChannel())  # ✅ WhatsAppChannel added
service.send("Hello again!")
# 📧 Email sent: Hello again!
# 💬 WhatsApp sent: Hello again!

# Try this with inheritance — you can't.
# You would need to instantiate a completely different class.


# ─────────────────────────────────────────────
# KEY TAKEAWAY
# ─────────────────────────────────────────────

# Inheritance asks:  "What ARE you?"
#   → EmailAndSMSNotification IS A Notification
#
# Composition asks:  "What do you HAVE?"
#   → Notification HAS an Email channel and an SMS channel
#
# When behavior needs to be COMBINED or CHANGED at runtime:
#   → Composition wins every time.
#
# Rule of thumb:
#   Inheritance  → for shared identity  ("is a")
#   Composition  → for shared behavior  ("has a")
#   Use inheritance when there is a true "is-a" relationship and the behavior is stable.
#   Use composition when features can be mixed, replaced, enabled, or disabled independently.
