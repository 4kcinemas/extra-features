from pyrogram import Client, filters

Client(
    "Netflix Bot",
    api_id="11762352",
    api_hash="2903597c04eb4a6d799ff8ffc87d4aac",
    bot_token="5222423549:AAFpbj40J4lgKgdbGbUl76HqUvFgtScA9DE"
)

@Client.on_message(filters.command("about"))
async def about_message(bot, message):
    await message.reply_text("➢ 𝐌𝐲 𝐍𝐚𝐦𝐞: 𝗡𝗘𝗧𝗙𝗟𝗜𝗫
    
➢ 𝐌𝐲 𝐂𝐫𝐞𝐚𝐭𝐨𝐫: <a href='https://t.me/sarathi_admin'>🅢︎🅐︎🅡︎🅐︎🅣︎🅗︎🅘︎[𝖲𝖲𝖫𝗂𝗇𝗄𝗓]</a>

➢ 𝐌𝐲 𝐒𝐨𝐮𝐫𝐜𝐞: <a href='https://github.com/EvamariaTG/EvaMaria'>Eva Maria</a>

➢ 𝐌𝐲 𝐋𝐢𝐛𝐫𝐚𝐫𝐲: 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆

➢ 𝐌𝐲 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: 𝖯𝗒𝗍𝗁𝗈𝗇3

➢ 𝐌𝐲 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞: 𝖬𝗈𝗇𝗀𝗈 𝖣𝖡 

➢ 𝐌𝐲 𝐒𝐞𝐫𝐯𝐞𝐫: 𝖧𝖾𝗋𝗈𝗄𝗎

➢ 𝐌𝐲 𝐔𝐩𝐝𝐚𝐭𝐞𝐬: <a href='https://t.me/ss_linkz'>𝖲𝖲 𝖫𝗂𝗇𝗄𝗓</a>

➢ 𝐌𝐲 𝐒𝐮𝐩𝐩𝐨𝐫𝐭: <a href='https://t.me/sslinkzsupport'>𝖲𝖲 𝖫𝗂𝗇𝗄𝗓 𝖲𝗎𝗉𝗉𝗈𝗋𝗍</a>

➤ 𝙸𝚏 𝚢𝚘𝚞 𝚕𝚒𝚔𝚎 𝚝𝚑𝚒𝚜 𝚋𝚘𝚝 𝚙𝚕𝚎𝚊𝚜𝚎 𝚜𝚑𝚊𝚛𝚎 𝚊𝚗𝚍 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 𝚞𝚜 ⚡"
            buttons= [[
            InlineKeyboardButton('𝖦𝗂𝗍𝖧𝗎𝖻', url='https://GitHub.com/EvaMariaTG/EvaMaria'),
            InlineKeyboardButton('𝖲𝗍𝖺𝗍𝗎𝗌', callback_data='stats'),
            InlineKeyboardButton('𝖢𝗅𝗈𝗌𝖾', callback_data='close_data')
        ]])



Client.run()
