user = {
    "id": 10,
    "name": "Mahmoud",
    "email": "mahmoud@example.com",
    # "contact": {
    #     "email": "mahmoud@example.com"
    # },
    "address": "Some address",
    "preferences": {},
}


def send_email(email: str) -> None:
    print(f"Sending email to {email}")


send_email(user["email"])
# send_email(user['contact']['email'])
