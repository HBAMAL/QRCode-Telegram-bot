from pyrogram import Client, filters
from messages import Msg
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """
Hello {}, I am a google translator telegram bot.
Made by @FayasNoushad
"""
HELP_TEXT = """
- Just send a text with language code
example :- `This is a sample text | ml`
Made by @FayasNoushad
"""
ABOUT_TEXT = """
- **Bot :** `Translator Bot`
- **Creator :** [Fayas](https://telegram.me/TheFayas)
- **Channel :** [Fayas Noushad](https://telegram.me/FayasNoushad)
- **Source :** [Click here](https://github.com/FayasNoushad/Translator-Bot)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
CLOSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Close', callback_data='close')
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
@Client.on_message(filters.command("start"))
async def start_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{Msg.start}{Msg.source}",
        reply_to_message_id=message.message_id,
    )

@Client.on_message(filters.command(["help", "h"]))
async def help_message(client, message):
    await client.send_message(  
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{Msg.help}{Msg.source}",
        reply_to_message_id=message.message_id,
    )
