from twilio_keys import *
from twilio.rest import Client


client = Client(account_sid, auth_token)


def send_text_message(name, phone_num, msg):
    print(name, phone_num, msg)
    message = client.messages.create(
        to = phone_num,
        from_= twilio_number,
        body = msg)

    print('Message sent to ', name)


def send_voice_msg(name, phone_num):
    client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=phone_num,
        from_=twilio_number
    )

    print('Voice message sent to', name)