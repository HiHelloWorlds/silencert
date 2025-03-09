from pyrogram import Client, filters

import os
from pyrogram import Client

session_string = os.getenv("SESSION_STRING")
app = Client(session_string=session_string)

@app.on_message(filters.group)
def delete_unwanted_message(client, message):
    print(message)
    unwanted_messages = [
        message.new_chat_members,
        message.left_chat_member,
        message.new_chat_title,
    ]
    for unwanted in unwanted_messages:
        if unwanted is not None:
            client.delete_messages(message.chat.id, [message.message_id])

    if message.text is not None and message.text.find("https://t.me/joinchat/") > -1:
        member = client.get_chat_member(message.chat.id, message.from_user.id)
        if not (member.status == "creator" or member.status == "administrator"):
            client.delete_messages(message.chat.id, [message.message_id])  # Delete none admin invitation


app.run()
