from pyrogram import Client, filters
from pyrogram.types import Message


api_id = api id
api_hash = 'api hash'
token = "token"


Client = Client("messageviewcounterbot", api_id, api_hash, bot_token=token)


forwardchannel = channel id
startmsg  = """
text
"""


@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply(startmsg,
)

@Client.on_message(~filters.service & ~filters.game & ~filters.channel & ~filters.edited & ~filters.linked_channel)
async def viewcounter(client, message):
    forward = await message.forward(forwardchannel)
    await forward.forward(message.chat.id)
    
    
Client.run()
