from twilio.rest import TwilioRestClient


account_sid = "AC0bcd7ce3b4dfef5983ee48a0189618d8"
auth_token = "c3c87709f501e8018bae7275d929db6f"

client = TwilioRestClient(account_sid, auth_token)
number_to_text = "+14158664966"
twilio_number = "+14803761510"

message = client.messages.create(to=number_to_text, from_=twilio_number, body="Hello there!")