
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hey there! I'm [Stella](https://telegra.ph/file/cc41cf2eebde1c4c0a0dd.jpg)** ✨
I Play and Download music on Telegram. To know how to use me, click on the **Initial Setup** button below!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚙️ Initial Setup", callback_data="cbhowtouse"),
                ],
                [
                    InlineKeyboardButton("❓ Help", callback_data="cbcmds"),
                    InlineKeyboardButton("💬 Support", url=f"https://t.me/MusicUpdates_Chat"),
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add me to your chat", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Stella's Help menu**

• Press the button below to read the Explanation and See the list of **Available Commands!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻‍♀ Basic cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("🕵🏻‍♀ Advanced", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("👮🏻‍♀ Admin", callback_data="cbadmin"),
                    InlineKeyboardButton("🧕🏻 Sudo", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("👩🏻‍🔧 Owner cmd", callback_data="cbowner")],
                [InlineKeyboardButton("« Back", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Here is the Basic Commands**

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Here is the Advanced Commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other­­­­­­­­­­­""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**👮🏻‍♀ Admin Commands:**

/player - Show the music playing status
/pause - Pause the music streaming
/resume - Resume the music was paused
/skip - Skip to the next song
/end - Stop music streaming
/join - Invite userbot join to your group
/leave - Order the userbot to leave


✅ <u>**Specific Skip:**</u>
/skip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

✅ <u>**Player Settings:**</u>
/control - Open the player settings panel
/delcmd (on/off) - Enable/Disable del cmd feature
/music (on/off) - Disable/Enable music player in your group

✅ <u>**Auth Users:**</u>
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Here is the Sudo Commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/clear - remove all .jpg files
/eval (query) - execute code
/sh (query) - run code""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**❗️ Vinuth's Commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

Note: All commands owned by this bot can be Executed by the Owner of the bot without any Exceptions.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **How to use Stella girl**

• First, add me to your group.
• Then promote me as admin and give all permissions except anonymous admin.
• After promoting me, type /reload in group to update the admin list.
• Add @{ASSISTANT_NAME} to your group or type /join to invite.
• Turn on the video chat first before start to play music.

If the userbot not joined to video chat, Make sure if the video chat already turned on, or type /leave then type /join again..


• [Support](https://t.me/MusicUpdates_Chat) | • [Updates Channel](https://t.me/The_Roboton) 
• Bot Developer [Vinuth](http://t.me/ImVinuth)

🔄 Stella has been online since ```2022/2/14```""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📚 Command List", callback_data="cbhelp")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin can tap this button !", show_alert=True)
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin can tap this button !", show_alert=True)
    await query.edit_message_text(
        f"""📚 **this is the feature information:**
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Stella's Help menu**

• Press the button below to read the Explanation and See the list of **Available Commands!­­­­­­­­­­­**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻‍♀ Basic cmd", callback_data="cblocal"),
                    InlineKeyboardButton("🕵🏻‍♀ Advanced", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("👮🏻‍♀ Admin", callback_data="cblamp"),
                    InlineKeyboardButton("🧕🏻 Sudo", callback_data="cblab"),
                ],
                [InlineKeyboardButton("👩🏻‍🔧 Owner cmd", callback_data="cbmoon")],
                [InlineKeyboardButton("« Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **How to use Stella girl**

• First, add me to your group.
• Then promote me as admin and give all permissions except anonymous admin.
• After promoting me, type /reload in group to update the admin list.
• Add @{ASSISTANT_NAME} to your group or type /join to invite.
• Turn on the video chat first before start to play music.

If the userbot not joined to video chat, Make sure if the video chat already turned on, or type /leave then type /join again..


• [Support](https://t.me/MusicUpdates_Chat) | • [Updates Channel](https://t.me/The_Roboton) 
• Bot Developer [Vinuth](http://t.me/ImVinuth)

🔄 Stella has been online since ```2022/2/14```""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Here is the Basic Commands**

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper­­­­­­­­­­­""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Here is the Advanced Commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**👮🏻‍♀ Admin Commands:**

/player - Show the music playing status
/pause - Pause the music streaming
/resume - Resume the music was paused
/skip - Skip to the next song
/end - Stop music streaming
/join - Invite userbot join to your group
/leave - Order the userbot to leave


✅ <u>**Specific Skip:**</u>
/skip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

✅ <u>**Player Settings:**</u>
/control - Open the player settings panel
/delcmd (on/off) - Enable/Disable del cmd feature
/music (on/off) - Disable/Enable music player in your group

✅ <u>**Auth Users:**</u>
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Here is the Sudo Commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/clear - remove all .jpg files
/eval (query) - execute code
/sh (query) - run code""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**❗️ Vinuth's Commands**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

Note: All commands owned by this bot can be Executed by the Owner of the bot without any Exceptions.­­­­­­­­­­­""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cmdhome"))
async def cmdhome(_, query: CallbackQuery):
    
    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Command Syntax", callback_data="cmdsyntax")
            ],[
                InlineKeyboardButton("🗑 Close", callback_data="close")
            ]
        ]
    )
    
    nofound = "🙁 **couldn't find song you requested**\n\n» **please provide the correct song name or include the artist's name as well**"
    
    await query.edit_message_text(nofound, reply_markup=bttn)


@Client.on_callback_query(filters.regex("cmdsyntax"))
async def cmdsyntax(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Command Syntax** to play music on **Voice Chat:**

• `/play (query)` - for playing music via youtube
• `/ytp (query)` - for playing music directly via youtube""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("« Back", callback_data="cmdhome")]]
        ),
    )
