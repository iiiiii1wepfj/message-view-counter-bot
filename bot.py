from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    Poll,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)


api_id: int = api id
api_hash: str = "api hash"
token: str = "token"


app = Client('viewcounterbot', in_memory=True, api_id=api_id, api_hash=api_hash, bot_token=token)

non_anonymous_poll = filters.create(
    lambda *_: _[2].poll is not None and not _[2].poll.is_anonymous
)

forwardchannel = -1000000000000
startmsg: str = """
text
"""


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply(
        startmsg,
    )


@app.on_message(
    ~filters.service
    & ~filters.game
    & ~filters.channel
    & ~filters.edited
    & ~filters.linked_channel
    & ~non_anonymous_poll
)
async def viewcounter(client, message):
    forward = await message.forward(forwardchannel)
    await forward.forward(message.chat.id)
    await forward.delete()


@app.on_message(
    (filters.service | filters.game | filters.channel | non_anonymous_poll)
    & ~filters.edited
)
async def notsupported(client, message):
    await message.reply(
        "sorry but this type of message not supported (non anonymous polls or games (like @gamebot or @gamee) or message from channels or service messages)",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("delete this message", "deleterrormessage")]]
        ),
    )


@app.on_callback_query(filters.regex("^deleterrormessage"))
async def delerrmsg(client: app, cquery: CallbackQuery):
    await cquery.message.delete()


app.run()
