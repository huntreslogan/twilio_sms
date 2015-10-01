from twilio.rest import TwilioRestClient


account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = TwilioRestClient(account_sid, auth_token)
number_to_text = "XXXXXXXXXXX"
twilio_number = "XXXXXXXXXXX"

message = client.messages.create(to=number_to_text, from_=twilio_number, body="Hello there!")