from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """
</b>HI {}, I AM A QR CODE GENERATOR BOT 😊

MADE BY</b> @TELSABOTS 
"""
HELP_TEXT = """SENT ANY LINK OR TEXT AND WILL GENERATE QR CODE

</b>SENT AN IMAGE AND I WILL SACAN QR CODES</b>

"""
ABOUT_TEXT = """ 🤖<b>BOT🤖: QR CODE🤖</b>

📢<b>CHANNEL :</b> ❤️ <a href='https://t.me/telsabots'>TELSA BOTS❤️</a>

🧑🏼‍💻DEV🧑🏼‍💻  : @ALLUADDICT



"""
JOIN_TEXT = """</b>❤️JOIN THESE CHANNELS ❤️
❤️ SHARE AND SUPPORT ❤️</b>"""

SOURCE_TEXT = """</b>PRESS SOURCE BUTTON FOR SOURCE 
AND WATCH TOTOURIAL VIDEO IF YOU WANT ANY HELP</b>"""


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/telsaBOTS'),
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-qr-code-bot.html')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/telsaBOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/ALLUADDICT')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/telsaBOTS'),
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-qr-code-bot.html'),
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )

SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-qr-code-bot.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/embed/nfWjbuQqgJ')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )

JOIN_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/telsaBOTS'),
        InlineKeyboardButton('🎬MOVIES GROUP🎬', url='https://telegram.me/FILIMSMOVIE')
        ],[
        InlineKeyboardButton('🎬MOVIES CHANNEL📢', callback_data='https://t.me/joinchat/UZzc1UhZLUnvorhW'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/ALLUADDICT'),
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-qr-code-bot.html'),
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]] 
    )


@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
        
@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     

@Client.on_message(filters.command(["help", "h"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
@Client.on_message(filters.command(["about", "a"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     

@Client.on_message(filters.command(["join", "j"]))
async def join_message(bot, update):
    text = JOIN_TEXT
    reply_markup = JOIN_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     

@Client.on_message(filters.command(["Source", "s"]))
async def Source_message(bot, update):
    text = SOURCE_TEXT
    reply_markup = SOURCE_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
