from keys import ACCOUNT_SID, AUTH_TOKEN, PHONE, TWILIO_NUMBER
from twilio.rest import Client

account_sid = ACCOUNT_SID
auth_token = "AUTH_TOKEN"

client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                    body="Are you available for dinner tomorrow ?",
                    from_=TWILIO_NUMBER,
                    to=PHONE
                )

print("Message sent!!")
