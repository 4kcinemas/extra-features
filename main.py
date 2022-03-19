from pyrogram import Client, filters

Client(
    "Netflix Bot",
    api_id="11762352",
    api_hash="2903597c04eb4a6d799ff8ffc87d4aac",
    bot_token="5222423549:AAFpbj40J4lgKgdbGbUl76HqUvFgtScA9DE"
)

@Client.on_message(filters.command("about"))
async def about(bot, message):
    await message.reply(
            buttons= [[
            InlineKeyboardButton('𝖦𝗂𝗍𝖧𝗎𝖻', url='https://GitHub.com/EvaMariaTG/EvaMaria'),
            InlineKeyboardButton('𝖲𝗍𝖺𝗍𝗎𝗌', callback_data='stats'),
            InlineKeyboardButton('𝖢𝗅𝗈𝗌𝖾', callback_data='close_data')
        ]])



Client.run()
