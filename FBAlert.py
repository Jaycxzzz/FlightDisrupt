from fbchat import Client
from fbchat.models import *

jayc = '100001808431261'
shash = '100009109136017'

person = [jayc, shash]


def send_alert(msg):
    client = Client('jaycxzchuinz@gmail.com', 'Temp123!')

    for i in range(person.__len__()):
        # If we have a user id, we can use `fetchUserInfo` to fetch a `User` object
        user_id = person[i]
        user = client.fetchUserInfo(user_id)[user_id]
        print("user's name: {}".format(user.name))

        msg_id = client.send(Message(text=msg), thread_id=user_id, thread_type=ThreadType.USER)

        client.onMessageDelivered(msg_ids=msg_id,
                                  delivered_for=user.name,
                                  thread_id=user_id,
                                  thread_type=ThreadType.USER,
                                  ts=1)

    client.logout()
    print('Complete.')

# send_alert('Hello there')