from pyrogram import Client, filters
from time import sleep

api_id = 123
api_hash = "HASH"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

need_chat = 'ID CHAT'
your_text = 'TEXT'


@app.on_message(filters=filters.channel)
def new_channel_post(client, message):
    if message.chat.id == need_id:
        print('Увидел новое')
        id_to_reply = message.id
        print(id_to_reply)
        m = client.get_discussion_message(message.chat.id, message.id)
        m.reply(your_text)


app.run()

