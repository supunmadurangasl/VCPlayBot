from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAEIoptgxsnCvC-AQIlhOaS8QYpIVL4zFgACZwAD29t-AAE93xTvYUeRnx4E")
    await message.reply_text(
        f"""<b> Hey,👋 {message.from_user.first_name}!
\n Hello 👋 there! I can play music in voice chats of Telegeam Groups.
I have a lot of cool feature that will amaze you!
\nTo add in your group contact us at @slbotzone .
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 Music World 🎧 ", url="https://t.me/supunmasl",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨‍👨‍👦 Group 👨‍👨‍👦 ", url="https://t.me/slbotzone"
                    ),
                    InlineKeyboardButton(
                        " 🌀 Channel 🌀 ", url="https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA?sub_confirmation=1"
                    ),
                    InlineKeyboardButton(
                        "📦 Source code📦", url="https://github.com/supunmadurangasl/VCPlayBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group 🎙 ", url="https://t.me/vc_play_slbotzone_bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
          "👨‍💻Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 🌀 Channel 🌀", url="https://t.me/FreeNetSL"
                    ),
                    InlineKeyboardButton(
                        " 👨‍👨‍👦 Group 👨‍👨‍👦", url="https://t.me/slbotzone"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hey,{message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 🌀 Channel🌀 ", url="https://t.me/FreeNetSL"
                    ),
                    InlineKeyboardButton(
                        "👨‍Group 👨‍", url="https://t.me/slbotzone"
                    )
                ]
            ]
        )
    )    
