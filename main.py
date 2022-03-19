from pyrogram import client

app=client(
    "Netflix Bot",
    api_id="11762352",
    api_hash="2903597c04eb4a6d799ff8ffc87d4aac",
    bot_token="5222423549:AAFpbj40J4lgKgdbGbUl76HqUvFgtScA9DE"
)


@app.on_message(filters.command("about"))
async def about(bot, message):
    await message.reply(script.ABOUT_TXT)




app.run()
