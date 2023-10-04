import os
from twilio.rest import Client

def send_message(message_body, too_phone):
	account_sid = "AC81e5482d34d6d7b1fbd5982d591edf09"
	auth_token = "83438458c10dfede95ff561ba9a0f600"
	from_phone = "+18442094871"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	body=message_body,
	from_=from_phone,
	to=too_phone
)
