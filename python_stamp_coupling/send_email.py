def send_email(user: dict) -> None:
    print(f"Sending email to {user['email']}")


user = {
    "id": 10,
    "name": "Mahmoud",
    # "email": "mahmoud@example.com",
    "contact": {"email": "mahmoud@example.com"},
    "address": "Some address",
    "preferences": {},
}

send_email(user)
